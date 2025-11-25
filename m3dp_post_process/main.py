import shutil
from pathlib import Path

from fastapi import FastAPI, File, Form, Request, UploadFile
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.templating import Jinja2Templates

from .gcode_processor import GCodeParser, Optimizer

app = FastAPI(title="M3DP Post Process")

# Setup templates
BASE_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = BASE_DIR / "templates"
templates = Jinja2Templates(directory=str(TEMPLATES_DIR))

# Ensure upload directory exists
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)
OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """Render main upload interface.

    Args:
        request: FastAPI request object for template context

    Returns:
        HTMLResponse with Jinja2-rendered upload form
    """
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/upload", response_class=HTMLResponse)
async def upload_file(request: Request, file: UploadFile = File(...)):
    """Upload and parse G-code file, display initial metrics.

    Args:
        request: FastAPI request object
        file: Uploaded G-code file

    Returns:
        HTMLResponse with parsed segment count and original metrics
        (print time, material usage, travel distance)
    """
    if file.filename is None:
        raise ValueError("Uploaded file must have a filename")
    file_location = UPLOAD_DIR / file.filename
    with open(file_location, "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)

    # Parse to get initial stats
    parser = GCodeParser(file_path=file_location)
    parser.parse()

    # Calculate original metrics for comparison
    from .gcode_processor import Optimizer

    temp_optimizer = Optimizer(parser.segments)
    original_print_time = temp_optimizer._calculate_print_time(parser.segments)
    original_material_mm, original_material_grams = temp_optimizer._calculate_material_usage(
        parser.segments
    )

    return templates.TemplateResponse(
        "partials/upload_success.html",
        {
            "request": request,
            "filename": file.filename,
            "segment_count": len(parser.segments),
            "original_print_time": original_print_time,
            "original_material_mm": original_material_mm,
            "original_material_grams": original_material_grams,
        },
    )


@app.post("/optimize", response_class=HTMLResponse)
async def optimize_file(
    request: Request,
    filename: str = Form(...),
    optimization_type: str = Form("travel"),  # "travel" or "bricklayers"
    algorithm: str = Form("greedy"),  # "greedy" or "aco" (for travel optimization)
    aco_variant: str = Form("mmas"),  # "original", "mmas", or "acs" (for ACO only)
    layer_height: float = Form(0.2),  # BrickLayers parameter
    extrusion_multiplier: float = Form(1.0),  # BrickLayers parameter
    # ACO parameters
    num_ants: int = Form(8),
    num_iterations: int = Form(8),
):
    """Apply optimization algorithm to uploaded G-code file.

    Supports three optimization types:
    1. Travel optimization (greedy or ACO algorithm)
    2. BrickLayers layer shifting for structural strength
    3. Quality improvements (seam hiding, shell crossing reduction)

    Args:
        request: FastAPI request object
        filename: Original uploaded filename
        optimization_type: 'travel', 'bricklayers', or 'quality'
        algorithm: 'greedy' or 'aco' (for travel optimization)
        layer_height: Layer height in mm (for BrickLayers)
        num_ants: Number of ants for ACO (default 8)
        num_iterations: ACO iteration count (default 8)

    Returns:
        HTMLResponse with optimization results, before/after metrics,
        and download link for optimized G-code
    """
    import logging

    logger = logging.getLogger("uvicorn")

    input_path = UPLOAD_DIR / filename
    output_filename = f"optimized_{filename}"
    output_path = OUTPUT_DIR / output_filename

    logger.info(
        f"🚀 Starting optimization: type={optimization_type}, algorithm={algorithm}, variant={aco_variant if algorithm == 'aco' else 'N/A'}, file={filename}"
    )

    # Parse
    parser = GCodeParser(file_path=input_path)
    parser.parse()
    logger.info(f"📊 Parsed {len(parser.segments)} segments")

    # Calculate original metrics before optimization
    from .gcode_processor import Optimizer as MetricsOptimizer

    temp_optimizer_for_original = MetricsOptimizer(parser.segments)
    original_print_time = temp_optimizer_for_original._calculate_print_time(parser.segments)
    original_material_mm, original_material_grams = (
        temp_optimizer_for_original._calculate_material_usage(parser.segments)
    )
    logger.info(
        f"📈 Original metrics: time={original_print_time / 60:.1f}min, material={original_material_mm / 1000:.2f}m"
    )

    # Optimize based on type
    if optimization_type == "bricklayers":
        logger.info("🧱 Starting BrickLayers optimization...")
        from .bricklayers import BrickLayersConfig, BrickLayersOptimizer

        config = BrickLayersConfig(
            layer_height=layer_height, extrusion_multiplier=extrusion_multiplier
        )
        optimizer_bl = BrickLayersOptimizer(str(input_path), config)
        result = optimizer_bl.optimize(str(output_path))
        logger.info("✅ BrickLayers optimization complete")

        # File is already written by optimizer
        gcode_content = None
    else:  # Travel optimization
        logger.info(f"🛣️  Starting travel optimization with {algorithm} algorithm...")
        # Choose algorithm
        if algorithm == "aco":
            logger.info(
                f"🐜 ACO config: variant={aco_variant}, {num_ants} ants × {num_iterations} iterations"
            )
            from .aco_optimizer import ACOConfig, ACOOptimizer

            aco_config = ACOConfig(
                aco_variant=aco_variant, num_ants=num_ants, num_iterations=num_iterations
            )
            optimizer = ACOOptimizer(parser.segments, aco_config)
            result = optimizer.optimize()
            logger.info("✅ ACO optimization complete")

            # Use base Optimizer for G-code generation
            base_optimizer = Optimizer(parser.segments)
            gcode_content = base_optimizer.to_gcode(result.segments)
        else:  # greedy
            greedy_optimizer = Optimizer(parser.segments)
            result = greedy_optimizer.optimize_travel_greedy()
            logger.info("✅ Greedy optimization complete")
            gcode_content = greedy_optimizer.to_gcode(result.segments)

    # Write output file if not already written
    if gcode_content is not None:
        with open(output_path, "w") as f:
            f.write(gcode_content)

    return templates.TemplateResponse(
        "partials/optimization_result.html",
        {
            "request": request,
            "original_filename": filename,
            "optimized_filename": output_filename,
            "original_count": len(parser.segments),
            "optimized_count": len(result.segments),
            "optimization_type": result.optimization_type,
            "original_travel": f"{result.original_travel_dist:.2f}",
            "optimized_travel": f"{result.optimized_travel_dist:.2f}",
            "saved_travel": f"{result.original_travel_dist - result.optimized_travel_dist:.2f}",
            "metadata": result.metadata,
            "print_time_seconds": result.print_time_seconds,
            "material_used_mm": result.material_used_mm,
            "material_used_grams": result.material_used_grams,
            "original_print_time": original_print_time,
            "original_material_mm": original_material_mm,
            "original_material_grams": original_material_grams,
        },
    )


@app.get("/download/{filename}")
async def download_file(filename: str):
    """Serve optimized G-code file for download.

    Args:
        filename: Name of optimized file in outputs/ directory

    Returns:
        FileResponse with application/octet-stream content type
    """
    file_path = OUTPUT_DIR / filename
    return FileResponse(file_path, filename=filename)


@app.get("/files/{filename}")
async def serve_file(filename: str):
    """Serve uploaded G-code file.

    Args:
        filename: Name of file in uploads/ directory

    Returns:
        FileResponse with text/plain content type
    """
    file_path = UPLOAD_DIR / filename
    return FileResponse(file_path)

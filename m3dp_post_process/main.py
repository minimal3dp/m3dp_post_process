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
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/upload", response_class=HTMLResponse)
async def upload_file(request: Request, file: UploadFile = File(...)):
    file_location = UPLOAD_DIR / file.filename
    with open(file_location, "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)

    # Parse to get initial stats
    parser = GCodeParser(file_path=file_location)
    parser.parse()

    return templates.TemplateResponse(
        "partials/upload_success.html",
        {"request": request, "filename": file.filename, "segment_count": len(parser.segments)},
    )


@app.post("/optimize", response_class=HTMLResponse)
async def optimize_file(
    request: Request,
    filename: str = Form(...),
    optimization_type: str = Form("travel"),  # "travel" or "bricklayers"
    algorithm: str = Form("greedy"),  # "greedy" or "aco" (for travel optimization)
    layer_height: float = Form(0.2),  # BrickLayers parameter
    extrusion_multiplier: float = Form(1.0),  # BrickLayers parameter
    # ACO parameters
    num_ants: int = Form(8),
    num_iterations: int = Form(8),
    # Quality parameters
    seam_hiding: bool = Form(False),
    seam_strategy: str = Form("random"),  # "random", "aligned", "rear"
    reduce_crossings: bool = Form(True),
):
    input_path = UPLOAD_DIR / filename
    output_filename = f"optimized_{filename}"
    output_path = OUTPUT_DIR / output_filename

    # Parse
    parser = GCodeParser(file_path=input_path)
    parser.parse()

    # Optimize based on type
    if optimization_type == "bricklayers":
        from .bricklayers import BrickLayersOptimizer, BrickLayersConfig

        config = BrickLayersConfig(
            layer_height=layer_height,
            extrusion_multiplier=extrusion_multiplier
        )
        optimizer_bl = BrickLayersOptimizer(str(input_path), config)
        result = optimizer_bl.optimize(str(output_path))
        
        # File is already written by optimizer
        gcode_content = None
    else:  # Travel optimization
        # Choose algorithm
        if algorithm == "aco":
            from .aco_optimizer import ACOOptimizer, ACOConfig
            
            aco_config = ACOConfig(
                num_ants=num_ants,
                num_iterations=num_iterations
            )
            optimizer = ACOOptimizer(parser.segments, aco_config)
            result = optimizer.optimize()
        else:  # greedy
            optimizer = Optimizer(parser.segments)
            result = optimizer.optimize_travel_greedy()
        
        # Apply quality optimizations if requested
        if seam_hiding or reduce_crossings:
            from .quality_optimizer import QualityOptimizer, QualityConfig, SeamStrategy
            
            # Map string to enum
            seam_strat = SeamStrategy.DISABLED
            if seam_hiding:
                seam_strat = {
                    "random": SeamStrategy.RANDOM,
                    "aligned": SeamStrategy.ALIGNED,
                    "rear": SeamStrategy.REAR,
                }.get(seam_strategy, SeamStrategy.RANDOM)
            
            quality_config = QualityConfig(
                seam_strategy=seam_strat,
                reduce_shell_crossings=reduce_crossings
            )
            quality_opt = QualityOptimizer(result.segments, quality_config)
            quality_result = quality_opt.optimize()
            
            # Merge metadata
            if result.metadata is None:
                result.metadata = {}
            if quality_result.metadata:
                result.metadata.update(quality_result.metadata)
            result.segments = quality_result.segments
        
        # Generate G-code for travel optimization
        gcode_content = optimizer.to_gcode(result.segments)

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
        },
    )


@app.get("/download/{filename}")
async def download_file(filename: str):
    file_path = OUTPUT_DIR / filename
    return FileResponse(file_path, filename=filename)

@app.get("/files/{filename}")
async def get_file(filename: str):
    file_path = UPLOAD_DIR / filename
    return FileResponse(file_path)

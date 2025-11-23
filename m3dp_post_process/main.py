from fastapi import FastAPI, Request, UploadFile, File, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
import shutil
import os
from pathlib import Path
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
    
    return templates.TemplateResponse("partials/upload_success.html", {
        "request": request,
        "filename": file.filename,
        "segment_count": len(parser.segments)
    })

@app.post("/optimize", response_class=HTMLResponse)
async def optimize_file(request: Request, filename: str = Form(...)):
    input_path = UPLOAD_DIR / filename
    output_filename = f"optimized_{filename}"
    output_path = OUTPUT_DIR / output_filename
    
    # Parse
    parser = GCodeParser(file_path=input_path)
    parser.parse()
    
    # Optimize
    optimizer = Optimizer(parser.segments)
    optimized_segments = optimizer.optimize_travel_greedy()
    
    # Generate G-code
    gcode_content = optimizer.to_gcode(optimized_segments)
    
    with open(output_path, "w") as f:
        f.write(gcode_content)
        
    return templates.TemplateResponse("partials/optimization_result.html", {
        "request": request,
        "original_filename": filename,
        "optimized_filename": output_filename,
        "original_count": len(parser.segments),
        "optimized_count": len(optimized_segments)
    })

@app.get("/download/{filename}")
async def download_file(filename: str):
    file_path = OUTPUT_DIR / filename
    return FileResponse(file_path, filename=filename)

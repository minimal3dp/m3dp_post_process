import os

from fastapi.testclient import TestClient

from m3dp_post_process.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "M3DP G-Code Optimizer" in response.text


def test_upload_and_optimize():
    # Create a dummy G-code file
    gcode_content = "G1 X10 Y10 E0.5\nG1 X20 Y10 E1.0"
    filename = "test_upload.gcode"

    with open(filename, "w") as f:
        f.write(gcode_content)

    try:
        # Test Upload
        with open(filename, "rb") as f:
            response = client.post("/upload", files={"file": (filename, f, "text/plain")})

        assert response.status_code == 200
        assert "File Uploaded Successfully!" in response.text
        assert filename in response.text

        # Test Optimize
        response = client.post("/optimize", data={"filename": filename})
        assert response.status_code == 200
        assert "Optimization Complete!" in response.text
        assert f"optimized_{filename}" in response.text

        # Test Download
        response = client.get(f"/download/optimized_{filename}")
        assert response.status_code == 200
        assert "Optimized by M3DP Post Process" in response.text
        
        # Test File Serving (for Viewer)
        response = client.get(f"/files/{filename}")
        assert response.status_code == 200
        assert "G1 X10 Y10" in response.text
        
    finally:
        # Cleanup
        if os.path.exists(filename):
            os.remove(filename)
        if os.path.exists(f"uploads/{filename}"):
            os.remove(f"uploads/{filename}")
        if os.path.exists(f"outputs/optimized_{filename}"):
            os.remove(f"outputs/optimized_{filename}")

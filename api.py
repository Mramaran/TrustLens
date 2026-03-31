# ============================================================================
# TrustLens - API Backend
# Developed by: Hack Elite
# ============================================================================

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
import uvicorn
import io
import os
from model_loader import analyze_image, load_models

# Initialize App
app = FastAPI(
    title="TrustLens API",
    description="Backend API for TrustLens AI Image Detection System",
    version="1.0.0"
)

# CORS Middleware (Allow extension to access)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify extension ID
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Preload models on startup
@app.on_event("startup")
async def startup_event():
    load_models()

@app.get("/")
async def root():
    return {"message": "TrustLens API is running", "status": "active"}

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    file_path = "extension/icons/icon48.png"
    if os.path.exists(file_path):
        return FileResponse(file_path)
    return {"status": "no icon found"}

@app.post("/analyze")
async def analyze(
    file: UploadFile = File(...), 
    model: str = "cnn"
):
    """
    Analyze an uploaded image.
    model: 'cnn', 'efficientnet', 'efficientnet_art'
    """
    if model not in ['cnn', 'efficientnet', 'efficientnet_art']:
        raise HTTPException(status_code=400, detail="Invalid model type")
    
    try:
        contents = await file.read()
        image_stream = io.BytesIO(contents)
        result = analyze_image(image_stream, model_type=model)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)

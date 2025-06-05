from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from fastapi.responses import JSONResponse
from src.modules.analysis.service import AnalysyssService

router = APIRouter(prefix="/analysis", tags=["analysis"])

@router.post("/upload_audio/")
async def upload_audio(file: UploadFile = File(...), analysis_service: AnalysyssService = Depends()):
    try:
        result = await analysis_service.handle_audio_upload(file)
        return JSONResponse(content={
            "message": "Archivo subido exitosamente",
            **result
        })
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al subir el archivo: {str(e)}")

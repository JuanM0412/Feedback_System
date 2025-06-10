from fastapi import APIRouter, UploadFile, File, HTTPException, Depends, Request
from fastapi.responses import JSONResponse
from src.models.user import User
from src.modules.analysis.service import AnalysyssService
from src.modules.auth.dependencies import get_current_user

router = APIRouter(prefix="/analysis", tags=["analysis"])

@router.post("/upload_audio/")
async def upload_audio(request: Request, file: UploadFile = File(...), analysis_service: AnalysyssService = Depends(), current_user: User = Depends(get_current_user)):
    try:
        result = await analysis_service.handle_audio_upload(file, current_user)
        await analysis_service.trigger_webhook(result, current_user)
        return JSONResponse(content={
            "message": "Archivo subido exitosamente",
            **result
        })
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al subir el archivo: {str(e)}")

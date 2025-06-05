import tempfile, os
from fastapi import UploadFile
from src.utils.google_drive import upload_file_to_drive

class AnalysyssService:
    def __init__(self):
        pass

    async def handle_audio_upload(self, file: UploadFile) -> dict:
        if not file.content_type.startswith('audio/'):
            raise ValueError("El archivo debe ser de audio")

        tmp_path = None

        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
                content = await file.read()
                tmp.write(content)
                tmp_path = tmp.name

            file_id = upload_file_to_drive(
                file_path=tmp_path,
                file_name=file.filename,
                mime_type=file.content_type
            )

            return {
                "file_id": file_id,
                "file_name": file.filename
            }

        finally:
            if tmp_path and os.path.exists(tmp_path):
                os.unlink(tmp_path)

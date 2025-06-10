from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from pathlib import Path
from src.core.config import settings
import os

BASE_DIR = Path(__file__).parent
SCOPES = [settings.SCOPES]
SERVICE_ACCOUNT_FILE = os.path.join(BASE_DIR, settings.SERVICE_ACCOUNT_FILE)

def get_drive_service():
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,
        scopes=SCOPES
    )
    return build('drive', 'v3', credentials=credentials)

def upload_file_to_drive(file_path: str, file_name: str, mime_type: str, folder_id: str = settings.FOLDER_ID):
    service = get_drive_service()
    
    file_metadata = {'name': file_name}
    if folder_id:
        file_metadata['parents'] = [folder_id]
    
    media = MediaFileUpload(file_path, mimetype=mime_type, resumable=True)

    file = service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()

    return file.get('id')

def create_folder(folder_name: str, parent_folder_id: str = None):
    service = get_drive_service()
    
    file_metadata = {
        'name': folder_name,
        'mimeType': 'application/vnd.google-apps.folder'
    }
    if parent_folder_id:
        file_metadata['parents'] = [parent_folder_id]
    
    folder = service.files().create(
        body=file_metadata,
        fields='id'
    ).execute()

    return folder.get('id')

def create_sheet(sheet_name: str, folder_id: str):
    service = get_drive_service()
    
    file_metadata = {
        'name': sheet_name,
        'mimeType': 'application/vnd.google-apps.spreadsheet'
    }
    if folder_id:
        file_metadata['parents'] = [folder_id]
    
    spreadsheet = service.files().create(
        body=file_metadata,
        fields='id'
    ).execute()

    return spreadsheet.get('id')

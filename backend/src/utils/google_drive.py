import os
from pathlib import Path

from google.oauth2 import service_account
from googleapiclient.discovery import build
from fastapi import HTTPException
from googleapiclient.http import MediaFileUpload

from src.core.config import settings

BASE_DIR = Path(__file__).parent
SCOPES = settings.SCOPES.split(",")
SERVICE_ACCOUNT_FILE = os.path.join(BASE_DIR, settings.SERVICE_ACCOUNT_FILE)


def get_drive_service():
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,
        scopes=SCOPES
    )
    return build('drive', 'v3', credentials=credentials)


def get_sheets_service():
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,
        scopes=SCOPES
    )
    return build('sheets', 'v4', credentials=credentials)


def upload_file_to_drive(file_path: str, file_name: str,
                         mime_type: str, folder_id: str = settings.FOLDER_ID):
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


def share_with_user(folder_id: str, email: str):
    try:
        service = get_drive_service()

        permission = {
            'type': 'user',
            'role': 'reader',
            'emailAddress': email
        }

        service.permissions().create(
            fileId=folder_id,
            body=permission,
            fields='id',
            sendNotificationEmail=True
        ).execute()
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error sharing folder with user {email}. User must have a Google account."
        )


def create_folder(folder_name: str, parent_folder_id: str = None,
                  user_mail: str = None):
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

    folder_id = folder.get('id')

    if user_mail:
        share_with_user(folder_id, user_mail)

    return folder_id


def create_sheet(sheet_name: str, folder_id: str):
    drive_service = get_drive_service()
    file_metadata = {
        'name': sheet_name,
        'mimeType': 'application/vnd.google-apps.spreadsheet'
    }
    if folder_id:
        file_metadata['parents'] = [folder_id]

    spreadsheet = drive_service.files().create(
        body=file_metadata,
        fields='id'
    ).execute()

    spreadsheet_id = spreadsheet.get('id')

    sheets_service = get_sheets_service()

    values = [
        ["Fecha", "Llamada", "Sentimiento", "Recomendaciones", "Análisis", "Evaluación"]
    ]

    body = {
        'values': values
    }

    sheets_service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id,
        range="A1",
        valueInputOption="RAW",
        body=body
    ).execute()

    return spreadsheet_id

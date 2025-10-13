import requests
import json
from google.oauth2 import service_account
from google.auth.transport.requests import Request

# Ruta al archivo JSON descargado desde Firebase
SERVICE_ACCOUNT_FILE = "credenciales.json"
PROJECT_ID = "appmobile-e16c2"

def obtener_token_acceso():
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,
        scopes=["https://www.googleapis.com/auth/firebase.messaging"],
    )
    credentials.refresh(Request())
    return credentials.token

def enviar_notificacion(token, titulo, cuerpo):
    url = f"https://fcm.googleapis.com/v1/projects/{PROJECT_ID}/messages:send"
    headers = {
        "Authorization": f"Bearer {obtener_token_acceso()}",
        "Content-Type": "application/json; UTF-8",
    }
    message = {
        "message": {
            "token": token,
            "notification": {
                "title": titulo,
                "body": cuerpo,
            }
        }
    }

    response = requests.post(url, headers=headers, data=json.dumps(message))
    try:
        return response.json()
    except:
        return {"status": "error", "text": response.text}

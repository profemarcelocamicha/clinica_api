import os
import json
import requests
from google.oauth2 import service_account
from google.auth.transport.requests import Request

# ID de tu proyecto Firebase
PROJECT_ID = "appmobile-e16c2"

def obtener_token_acceso():
    # Leer las credenciales desde la variable de entorno
    credenciales_json = os.getenv("FIREBASE_CREDENTIALS_JSON")

    if not credenciales_json:
        raise ValueError("❌ No se encontró la variable de entorno FIREBASE_CREDENTIALS_JSON")

    # Parsear el JSON (que está almacenado como texto en la variable de entorno)
    cred_dict = json.loads(credenciales_json)

    # Crear las credenciales desde el diccionario
    credentials = service_account.Credentials.from_service_account_info(
        cred_dict,
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

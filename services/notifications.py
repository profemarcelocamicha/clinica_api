import os
import json
import requests
from google.oauth2 import service_account
from google.auth.transport.requests import Request

# ID de tu proyecto Firebase
PROJECT_ID = "appmobile-e16c2"

def obtener_token_acceso():
    """
    Obtiene el token de acceso para usar Firebase Cloud Messaging (FCM),
    leyendo las credenciales desde Render o desde tu PC local.
    """

    # Render (Linux), el archivo en /etc/secrets/
    ruta_credenciales_render = "/etc/secrets/credenciales.json"

    # Windows en una ruta local
    ruta_credenciales_local = "C:\\api_turnos_db\\etc\\secrets\\credenciales.json"

    # Elegir la ruta según el entorno
    if os.path.exists(ruta_credenciales_render):
        ruta_credenciales = ruta_credenciales_render
        print("render")
    elif os.path.exists(ruta_credenciales_local):
        ruta_credenciales = ruta_credenciales_local
        print("local:", ruta_credenciales)        
    else:
        raise FileNotFoundError("❌ No se encontró el archivo de credenciales ni en Render ni en local.")

    # Leer el archivo JSON
    with open(ruta_credenciales, "r", encoding="utf-8") as archivo:
        cred_dict = json.load(archivo)

    # Crear las credenciales
    credentials = service_account.Credentials.from_service_account_info(
        cred_dict,
        scopes=["https://www.googleapis.com/auth/firebase.messaging"],
    )

    credentials.refresh(Request())
    return credentials.token


def enviar_notificacion(token, titulo, cuerpo):
    """
    Envía una notificación push usando Firebase Cloud Messaging (FCM).
    """
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
    except Exception:
        return {"status": "error", "text": response.text}

import os
import requests

def enviar_notificacion(token, titulo, cuerpo):
    fcm_server_key = os.getenv("FCM_SERVER_KEY")
    headers = {
        "Authorization": f"key={fcm_server_key}",
        "Content-Type": "application/json",
    }

    payload = {
        "to": token,
        "notification": {
            "title": titulo,
            "body": cuerpo,
        },
    }

    response = requests.post(
        "https://fcm.googleapis.com/fcm/send",
        headers=headers,
        json=payload
    )
    return response.json()

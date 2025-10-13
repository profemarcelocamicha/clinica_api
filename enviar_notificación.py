import requests

# URL de tu API en Render
API_URL = "https://clinica-api-0n5q.onrender.com/api/usuarios/notificar"

# Datos de prueba
payload = {
    "userId": "1",  # Reemplazá con el user_id real del usuario
    "titulo": "Turno confirmado",
    "cuerpo": "Tu turno fue confirmado para mañana a las 10:00"
}

response = requests.post(API_URL, json=payload)

print("Status code:", response.status_code)
print("Respuesta:", response.json())

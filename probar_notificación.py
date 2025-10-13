import requests

# URLs de la API
API_LISTAR = "https://clinica-api-0n5q.onrender.com/api/usuarios/listar"
API_NOTIFICAR = "https://clinica-api-0n5q.onrender.com/api/usuarios/notificar"

# Paso 1: listar usuarios
try:
    response = requests.get(API_LISTAR)
    response.raise_for_status()  # lanza error si status != 200
    usuarios = response.json().get("usuarios", [])
except requests.exceptions.RequestException as e:
    print("Error al consultar usuarios:", e)
    usuarios = []

if not usuarios:
    print("No hay usuarios registrados en la base.")
    exit()

# Mostrar usuarios
print("Usuarios registrados:")
for u in usuarios:
    print(f"- id: {u['user_id']}")

# Paso 2: seleccionar usuario
# user_id = usuarios[0]['user_id']  # tomamos el primer usuario como ejemplo
user_id = usuarios[0]['token_fcm']  # tomamos el primer usuario como ejemplo
# user_id = usuarios[0]['token_fcm']  # tomamos el primer usuario como ejemplo

print(f"\nEnviando notificación al usuario: {user_id}")

# Paso 3: preparar payload
payload = {
    "userId": user_id,
    "titulo": "Turno confirmado",
    "cuerpo": "Tu turno fue confirmado para mañana a las 10:00"
}

# Paso 4: enviar notificación
try:
    response = requests.post(API_NOTIFICAR, json=payload)
    print("Status code:", response.status_code)
    try:
        print("Respuesta:", response.json())
    except ValueError:
        print("La respuesta no es JSON:", response.text)
except requests.exceptions.RequestException as e:
    print("Error al enviar notificación:", e)

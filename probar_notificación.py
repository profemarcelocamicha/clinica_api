import requests
from services.notifications import enviar_notificacion

# URLs de la API
API_LISTAR = "https://clinica-api-0n5q.onrender.com/api/usuarios/usuarios"

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
    print(f"- id: {u['user_id']} {u['token_fcm']} ")

# Paso 2: seleccionar usuario
user_id = usuarios[0]['user_id']  # tomamos el primer usuario como ejemplo
token_fcm = usuarios[0]['token_fcm']  # tomamos el primer token como ejemplo

print(f"\nEnviando notificación al usuario: {user_id}")

token_fcm = "c3PXXOF3RimvCeo_ucqX9M:APA91bFlTB247CDWtrS-oBKj-74ktW3D0rGOUsxFAbR42eG3JvsdsS0MJMx8cCpbTDg0MZMQWJJfjLZhWWdNvmNiwoWQnYC1EylpwGIXCRID6kzdXTd25QY"
resultado = enviar_notificacion(token_fcm, "Hola 2", "Prueba desde HTTP v1 2")
print(resultado)

import requests

API_URL = "https://clinica-api-0n5q.onrender.com/api/usuarios/listar"

response = requests.get(API_URL)
print(response.json())

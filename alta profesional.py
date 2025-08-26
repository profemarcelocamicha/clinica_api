import requests

# url = 'http://localhost:5000/api/turnos'
url = 'https://clinica-api-0n5q.onrender.com/api/profesional'


data = {
    "nombre": "Leandro",
    "apellido": "Berberian",
    "fechaNac": "1993-08-23",
    "direccion": "Rivadavia 1978 - Haedo"
}


response = requests.post(url, json=data)
print(response.json())







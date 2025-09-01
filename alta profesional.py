import requests

# url = 'http://localhost:5000/api/turnos'
url = 'https://clinica-api-0n5q.onrender.com/api/profesional'


data = {
    "nombre": "Marcelo",
    "apellido": "Gomez",
    "fechaNac": "1995-08-23",
    "direccion": "Rivadavia 1986 - Morón"
}


response = requests.post(url, json=data)
print(response.json())







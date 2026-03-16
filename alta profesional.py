import requests

# url = 'http://localhost:5000/api/turnos'
url = 'https://clinica-api-0n5q.onrender.com/api/profesional'


data = {
    "nombre": "Pamela",
    "apellido": "Garay",
    "fechaNac": "1975-08-20",
    "direccion": "Olavarria 986 - Mar del Plata",
}


response = requests.post(url, json=data)
print(response.json())







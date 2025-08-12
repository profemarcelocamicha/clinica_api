import requests

# url = 'http://localhost:5000/api/turnos'
url = 'https://clinica-api-0n5q.onrender.com/api/turnos'


data = {
    "paciente": "Martín Gonzalez",
    "medico": "Dra. Chaparro",
    "fecha": "2025-08-22",
    "hora": "10:00"
}

response = requests.post(url, json=data)
print(response.json())




import requests

# url = 'http://localhost:5000/api/turnos'
url = 'https://clinica-api-0n5q.onrender.com/api/turnos'


data = {
    "paciente": "Juan Pérez",
    "medico": "Dra. López",
    "fecha": "2025-08-20",
    "hora": "10:30"
}

response = requests.post(url, json=data)
print(response.json())




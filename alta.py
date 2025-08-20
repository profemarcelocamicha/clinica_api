import requests

# url = 'http://localhost:5000/api/turnos'
url = 'https://clinica-api-0n5q.onrender.com/api/turnos'


data = {
    "paciente": "Marcelo Camicha",
    "medico": "Dr. Berberian",
    "fecha": "2025-08-23",
    "hora": "13:30"
}

response = requests.post(url, json=data)
print(response.json())




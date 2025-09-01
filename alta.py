import requests

# url = 'http://localhost:5000/api/turnos'
url = 'https://clinica-api-0n5q.onrender.com/api/turnos'


data = {
    "paciente": "Emma Rodriguez",
    "medico": "Dr. Fernandez Alberto",
    "fecha": "2025-10-03",
    "hora": "13:30"
}

response = requests.post(url, json=data)
print(response.json())




import requests

# url = 'http://localhost:5000/api/turnos'
url = 'https://clinica-api-0n5q.onrender.com/api/turnos'


data = {
    "paciente": "Nazareno Rodriguez",
    "medico": "Dr. Gimenez Alberto",
    "fecha": "2025-09-03",
    "hora": "13:00"
}

response = requests.post(url, json=data)
print(response.json())




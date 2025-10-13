import requests

# url = 'http://localhost:5000/api/turnos'
url = 'https://clinica-api-0n5q.onrender.com/api/turnos'


data = {
    "paciente": "Jose Contreras",
    "email": "jose@gmail.com",    
    "medico": "Dra. Barbara Donato",
    "fecha": "2025-09-13",
    "hora": "9:45"
}

response = requests.post(url, json=data)
print(response.json())




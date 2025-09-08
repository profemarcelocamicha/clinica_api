import requests

# url = 'http://localhost:5000/api/turnos'
url = 'https://clinica-api-0n5q.onrender.com/api/turnos'


data = {
    "paciente": "Jose Contreras",
    "email": "jose@gmail.com",    
    "medico": "Dr. Ismael Adorni",
    "fecha": "2025-09-12",
    "hora": "9:30"
}

response = requests.post(url, json=data)
print(response.json())




import requests

# url = 'http://localhost:5000/api/turnos'
url = 'https://clinica-api-0n5q.onrender.com/api/turnos'

data = {
    "paciente": "Milagros Gonzalez",
    "email": "milagrosgonzalez@gmail.com",    
    "medico": "Guillen Andres",
    "fecha": "2026-04-03",
    "hora": "8:00"
}

response = requests.post(url, json=data)
print(response.json())




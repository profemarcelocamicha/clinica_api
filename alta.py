import requests

# url = 'http://localhost:5000/api/turnos'
url = 'https://clinica-api-0n5q.onrender.com/api/turnos'


data = {
    "paciente": "Ana Rivas",
    "email": "ana@gmail.com",    
    "medico": "Dr. Torres Teodoro",
    "fecha": "2025-09-25",
    "hora": "9:00"
}

response = requests.post(url, json=data)
print(response.json())




import requests

# url = 'http://localhost:5000/api/turnos'
url = 'https://clinica-api-0n5q.onrender.com/api/turnos'

data = {
    "paciente": "Mili Pili",
    "email": "mili@gmail.com",    
    "medico": "Dra. Ripamontti Guillermina",
    "fecha": "2025-12-13",
    "hora": "9:45"
}

response = requests.post(url, json=data)
print(response.json())




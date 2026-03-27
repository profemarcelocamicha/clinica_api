#consulta_turnos.py
import requests

url = 'https://clinica-api-dev.onrender.com/api/turnos/1'

response = requests.get(url)
print(response.json())




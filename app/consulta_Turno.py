import requests

# url = 'https://clinica-api-0n5q.onrender.com/api/turnos/1'
url = 'https://clinica-api-dev.onrender.com/api/turnos/1'

response = requests.get(url)
print(response.json())




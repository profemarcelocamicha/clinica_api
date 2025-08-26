import requests

# url = 'http://localhost:5000/api/turnos/<id>'
url = 'https://clinica-api-0n5q.onrender.com/api/turnos/1'



response = requests.get(url)
print(response.json())




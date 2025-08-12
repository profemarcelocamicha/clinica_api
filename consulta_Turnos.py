import requests

# url = 'http://localhost:5000/api/turnos'
url = 'https://clinica-api-0n5q.onrender.com/api/turnos'



response = requests.get(url)
print(response.json())




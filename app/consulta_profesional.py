import requests

# url = 'http://localhost:5000/api/profesionales'
url = 'https://clinica-api-dev.onrender.com/api/profesionales'

response = requests.get(url)
print(response.json())




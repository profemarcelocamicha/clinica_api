import requests

url = 'https://clinica-api-dev.onrender.com/api/tablas'

response = requests.get(url)
print(response.json())




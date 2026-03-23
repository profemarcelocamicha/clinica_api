import requests

# url = "https://clinica-api-0n5q.onrender.com/api/usuarios"
url = "https://clinica-api-dev.onrender.com/api/usuarios"

response = requests.get(url)
print(response.json())

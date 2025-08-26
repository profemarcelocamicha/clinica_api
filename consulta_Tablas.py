import requests

url = 'https://clinica-api-0n5q.onrender.com/api/tablas'



response = requests.get(url)
print(response.json())




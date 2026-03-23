import requests

url = "https://clinica-api-dev.onrender.com/api/usuarios"
data = {
    "userId": "prueba123",
    "email": "test@gmail.com",
    "token_fcm": "abcdefg"
}
resp = requests.post(url, json=data)

print(resp.status_code)
print(resp.text)
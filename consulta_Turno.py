import requests

# url = 'http://localhost:5000/api/turnos/<id>'
url = 'https://clinica-api-0n5q.onrender.com/api/turnos/2'
def funcion1(){
    print("funcion1")
}

def funcion2(){
    print("funcion2")
}


response = requests.get(url)
print(response.json())




# archivo: alta_turno.py

import requests

# url = 'http://localhost:5000/api/turnos'
URL = 'https://clinica-api-0n5q.onrender.com/api/turnos'


def crear_turno(data, url=URL):
    response = requests.post(url, json=data)
    return response.json()


# 👇 Esto mantiene tu comportamiento actual (modo script)
if __name__ == "__main__":
    data = {
        "paciente": "Milagros Gonzalez",
        "email": "milagrosgonzalez@gmail.com",
        "medico": "Guillen Andres",
        "fecha": "2026-04-03",
        "hora": "8:00"
    }

    resultado = crear_turno(data)
    print(resultado)
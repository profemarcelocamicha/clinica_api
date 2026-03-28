import pytest
import os
from datetime import datetime
from app.alta_turno import crear_turno


@pytest.mark.integration
def test_crear_turno_real():
    # Obtener entorno (Render o local)
    env = os.getenv("ENV", "dev_local")

    # Fecha y hora actuales
    now = datetime.now()
    fecha_actual = now.strftime("%Y-%m-%d")
    hora_actual = now.strftime("%H:%M")

    data = {
        "paciente": f"Test {env.upper()}",
        "email": f"test_{env}@test.com",
        "medico": "Doc",
        "fecha": fecha_actual,
        "hora": hora_actual
    }

    response = crear_turno(data)

    assert "mensaje" in response
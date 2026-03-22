import pytest
from app.alta_turno import crear_turno


@pytest.mark.integration
def test_crear_turno_real():
    data = {
        "paciente": "Test Integracion",
        "email": "test@test.com",
        "medico": "Doc",
        "fecha": "2026-01-01",
        "hora": "10:00"
    }

    response = crear_turno(data)

    assert "mensaje" in response
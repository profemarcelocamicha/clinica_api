import pytest

@pytest.mark.integration
def test_crear_turno(client):
    response = client.post(
        "/turnos/",
        json={
            "nombre": "Ana",
            "fecha": "2026-03-17"
        }
    )

    assert response.status_code == 200

    data = response.json()
    assert data["nombre"] == "Ana"
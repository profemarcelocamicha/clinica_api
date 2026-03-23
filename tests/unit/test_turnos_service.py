import pytest
from app.alta_turno import crear_turno, URL  # Usar la constante del módulo para asegurar consistencia

@pytest.mark.unit
def test_crear_turno_mock(monkeypatch):

    llamada = {}  # para capturar lo que recibe requests.post

    def mock_post(*args, **kwargs):
        llamada["url"] = args[0]
        llamada["json"] = kwargs.get("json")

        class MockResponse:
            def json(self):
                return {"mensaje": "Turno creado correctamente"}
        return MockResponse()

    monkeypatch.setattr("requests.post", mock_post)

    data = {
        "paciente": "Test",
        "email": "test@test.com",
        "medico": "Doc",
        "fecha": "2026-01-01",
        "hora": "10:00"
    }

    response = crear_turno(data)

    # ✅ Validar respuesta
    assert response["mensaje"] == "Turno creado correctamente"

    # ✅ Validar URL usando constante (mejor práctica)
    assert llamada["url"] == URL

    # ✅ Validar JSON enviado
    assert llamada["json"] == data
import pytest
from app import models

@pytest.mark.unit
def test_crear_turno_model():
    turno = models.Turno(nombre="Juan", fecha="2026-03-17")

    assert turno.nombre == "Juan"
    assert turno.fecha == "2026-03-17"
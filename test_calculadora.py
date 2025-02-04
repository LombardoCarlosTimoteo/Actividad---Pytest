# test_calculadora.py
import pytest
from calculadora import Calculadora

@pytest.fixture
def calc():
    """Fixture para inicializar la calculadora antes de cada test."""
    return Calculadora()

@pytest.mark.parametrize("a, b, resultado", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0)
])
def test_suma(calc, a, b, resultado):
    assert calc.sumar(a, b) == resultado

@pytest.mark.parametrize("a, b, resultado", [
    (5, 3, 2),
    (0, 1, -1),
    (10, -5, 15)
])
def test_resta(calc, a, b, resultado):
    assert calc.restar(a, b) == resultado

@pytest.mark.parametrize("a, b, resultado", [
    (2, 3, 6),
    (-1, 1, -1),
    (0, 10, 0)
])
def test_multiplicacion(calc, a, b, resultado):
    assert calc.multiplicar(a, b) == resultado

def test_division(calc):
    assert calc.dividir(10, 2) == 5
    assert calc.dividir(9, 3) == 3
    with pytest.raises(ValueError, match="No se puede dividir por cero"):
        calc.dividir(5, 0)



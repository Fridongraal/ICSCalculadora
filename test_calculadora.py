from calculadora import sumar, restar, multiplicar, dividir
import pytest

def test_sumar():
    assert sumar(2, 3) == 5
    assert sumar(-1, 1) == 0

def test_restar():
    assert restar(5, 3) == 2
    assert restar(0, 5) == -5

def test_multiplicar():
    assert multiplicar(4, 3) == 12
    assert multiplicar(-2, 3) == -6

def test_dividir():
    assert dividir(10, 2) == 5
    assert dividir(7, 2) == 3.5

def test_dividir_por_cero():
    with pytest.raises(ValueError):
        dividir(10, 0)
import pytest
from calculadora_login import factorial, combinatoria, permutacion

def test_factorial_positivo():
    assert factorial(5) == 120
    assert factorial(1) == 1
    assert factorial(7) == 5040

def test_factorial_cero():
    assert factorial(0) == 1

def test_factorial_negativo():
    with pytest.raises(ValueError, match="El factorial no está definido para números negativos."):
        factorial(-1)
    with pytest.raises(ValueError, match="El factorial no está definido para números negativos."):
        factorial(-10)

def test_factorial_no_entero():
    with pytest.raises(ValueError, match="El factorial solo está definido para números enteros."):
        factorial(3.5)
    with pytest.raises(ValueError, match="El factorial solo está definido para números enteros."):
        factorial("abc")
    with pytest.raises(ValueError, match="El factorial solo está definido para números enteros."):
        factorial(None)

def test_factorial_limite_superior():
    """
    Test para el límite superior del factorial, usado en la demostración TDD.
    """
    with pytest.raises(ValueError, match="El número es demasiado grande para calcular el factorial."):
        factorial(171) # Usamos 171 ahora que el límite es 170


def test_combinatoria_valores_validos():
    assert combinatoria(5, 2) == 10
    assert combinatoria(4, 2) == 6
    assert combinatoria(7, 3) == 35
    assert combinatoria(4, 4) == 1
    assert combinatoria(5, 0) == 1

def test_combinatoria_n_menor_que_k():
    assert combinatoria(2, 5) == 0
    assert combinatoria(0, 1) == 0

def test_combinatoria_valores_negativos():
    with pytest.raises(ValueError, match="n y k deben ser números no negativos para la combinatoria."):
        combinatoria(-5, 2)
    with pytest.raises(ValueError, match="n y k deben ser números no negativos para la combinatoria."):
        combinatoria(5, -2)
    with pytest.raises(ValueError, match="n y k deben ser números no negativos para la combinatoria."):
        combinatoria(-5, -2)

def test_combinatoria_no_enteros():
    with pytest.raises(ValueError, match="n y k deben ser números enteros para la combinatoria."):
        combinatoria(5.5, 2)
    with pytest.raises(ValueError, match="n y k deben ser números enteros para la combinatoria."):
        combinatoria(5, 2.5)
    with pytest.raises(ValueError, match="n y k deben ser números enteros para la combinatoria."):
        combinatoria("a", 2)
    with pytest.raises(ValueError, match="n y k deben ser números enteros para la combinatoria."):
        combinatoria(5, "b")

# --- NUEVOS Tests para la función permutacion ---

def test_permutacion_valores_validos():
    assert permutacion(5, 2) == 20 # P(5,2) = 5! / 3! = 120 / 6 = 20
    assert permutacion(4, 2) == 12 # P(4,2) = 4! / 2! = 24 / 2 = 12
    assert permutacion(3, 3) == 6  # P(3,3) = 3! / 0! = 6 / 1 = 6  <-- ESTE ES EL QUE NOS INTERESA QUE FALLE
    assert permutacion(5, 0) == 1  # P(n,0) = 1


def test_permutacion_k_mayor_que_n():
    """Criterio: Manejar permutación con k > n."""
    with pytest.raises(ValueError, match="Para permutación P\\(n, k\\), k no puede ser mayor que n."):
        permutacion(2, 5)
    with pytest.raises(ValueError, match="Para permutación P\\(n, k\\), k no puede ser mayor que n."):
        permutacion(0, 1)

def test_permutacion_valores_negativos():
    """Criterio: Manejar permutación con valores negativos."""
    with pytest.raises(ValueError, match="n y k deben ser números no negativos para la permutación."):
        permutacion(-5, 2)
    with pytest.raises(ValueError, match="n y k deben ser números no negativos para la permutación."):
        permutacion(5, -2)
    with pytest.raises(ValueError, match="n y k deben ser números no negativos para la permutación."):
        permutacion(-5, -2)

def test_permutacion_no_enteros():
    """Criterio: Manejar permutación con valores no enteros."""
    with pytest.raises(ValueError, match="n y k deben ser números enteros para la permutación."):
        permutacion(5.5, 2)
    with pytest.raises(ValueError, match="n y k deben ser números enteros para la permutación."):
        permutacion(5, 2.5)
    with pytest.raises(ValueError, match="n y k deben ser números enteros para la permutación."):
        permutacion("a", 2)
    with pytest.raises(ValueError, match="n y k deben ser números enteros para la permutación."):
        permutacion(5, "b")
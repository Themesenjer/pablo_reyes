import pytest
from area import calculate_square_area

# Prueba que pasara
def test_area_correct():
    assert calculate_square_area(4) == 16

# Prueba que fallará para el 2do commit 
def test_negative_side_error():
    # Vamos a forzar un fallo *quitando* la excepción temporalmente
    # para el 2do commit y luego lo corregiremos.
    assert calculate_square_area(-5) == 25 # Esto es lo que va a fallar
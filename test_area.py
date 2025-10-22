import pytest
from area import calculate_square_area

# Prueba que pasará 
def test_area_correct():
    assert calculate_square_area(4) == 16

# Prueba que pasará (Test 2 - Corregida)
def test_negative_side_error():
    # El test debe verificar que la función LANCE un error, no que devuelva un valor
    with pytest.raises(ValueError, match="El lado no puede ser negativo."):
        calculate_square_area(-5)
# test_area.py (Corregido para que pase la CI)
import pytest
from area import calculate_square_area

def test_area_correct():
    assert calculate_square_area(4) == 16

# Esta es la corrección que hace que la prueba pase
def test_negative_side_error():
    with pytest.raises(ValueError, match="El lado no puede ser negativo."):
        calculate_square_area(-5)
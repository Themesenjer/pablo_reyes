# area.py
def calculate_square_area(side):
    """Calcula el área de un cuadrado. Debe ser un lado positivo."""
    if side < 0:
        raise ValueError("El lado no puede ser negativo.")
    return side * side

if __name__ == "__main__":
    print(f"Área de lado 5: {calculate_square_area(5)}")
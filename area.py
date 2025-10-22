# Este  es para que aparezaca en la web
from flask import Flask, request, jsonify

# Creamos la instancia de la aplicación Flask
app = Flask(__name__)

# Función original
def calculate_square_area(side):
    """Calcula el área de un cuadrado. Debe ser un lado positivo."""
    if side < 0:
        raise ValueError("El lado no puede ser negativo.")
    return side * side

# Creamos el endpoint web en la ruta /area
@app.route('/area', methods=['GET'])
def get_area():
    try:
        # Obtener el parámetro 'side' de la URL
        side = request.args.get('side', type=float)
        
        if side is None:
             raise ValueError("Falta el parámetro 'side'.")

        # Llamar a la función original
        result = calculate_square_area(side)
        
        # Devolver el resultado en formato JSON
        return jsonify({
            "status": "success",
            "side": side,
            "area": result
        }), 200

    except ValueError as e:
        # Maneja el error de lado negativo o parámetro faltante
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400
    except Exception as e:
        return jsonify({"status": "error", "message": "Error interno del servidor."}), 500


if __name__ == '__main__':
    # Hacemos que Flask escuche en el puerto 8080 (para mapeo de Docker)
    app.run(host='0.0.0.0', port=8080)
    #Todo esto ya esta modificado tambien en el servidor 
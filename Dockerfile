# Usamos la imagen base de Python en su version mas liguera
FROM python:3.10-slim

# Establecemos nuestro directorio de trabajo
WORKDIR /usr/src/app

# Copiamos el archivo de dependencias e instalar
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el código fuente
COPY . .

# Paso final: Informar que el contenedor usa el puerto 8080
EXPOSE 8080

# Comando de inicio: Este ejecuta la aplicación de forma simple
# Aqui es donde le damos un cambio para el commit final (CUARTO COMMIT)
# La aplicación calcula el área del cuadrado
CMD ["python", "area.py"]
#Todo esto ya esta en el servidor
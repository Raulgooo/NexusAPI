# 1. Imagen base con Python 3.13
FROM python:3.13-slim

# 2. Crear carpeta de trabajo
WORKDIR /app

# 3. Copiar requirements y instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copiar todo el código al contenedor
COPY . .

# 5. Exponer el puerto de FastAPI
EXPOSE 8000

# 6. Comando para levantar la app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

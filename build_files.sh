# Instala las dependencias
python -m pip install -r requirements.txt

# Ejecuta las migraciones y recolecta los archivos estáticos
python manage.py collectstatic --noinput
python manage.py migrate
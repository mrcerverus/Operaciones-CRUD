import os
import django
from django.db import connection

# Establecer la ruta base del proyecto Django
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

# Cambiar al directorio del proyecto Django
os.chdir(BASE_DIR)

from app.models import *

def fetch_data_from_db():
    # Consulta SQL para obtener inmuebles por comuna
    with connection.cursor() as cursor:
        #Consulta SQL
        query = """
            SELECT app_inmueble.nombre, app_inmueble.descripcion, app_comuna.name, app_region.name
            FROM app_inmueble
            INNER JOIN app_comuna ON app_comuna.id = app_inmueble.comuna_id
            INNER JOIN app_region ON app_region.id = app_comuna.region_id
                """

        cursor.execute(query)
        #Obtener todos los resultados
        rows = cursor.fetchall()
    return rows

def save_data_to_txt(rows, file_path):
    with open(file_path, 'w') as file:
        for row in rows:
            file.write(str(row) + '\n')

def export_data_to_txt():
    #Primero obtener datos de la base de datos
    rows = fetch_data_from_db()
    #Segundo, guardar los datos en una archivo de texto
    file_path = 'query.txt'
    save_data_to_txt(rows, file_path)

    print(f'Data saved to {file_path}')

if __name__ == "__main__":
    export_data_to_txt()
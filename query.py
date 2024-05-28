import os
import django
from django.db import connection

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

def export_inmuebles_por_comuna(file_path):
    # Consulta SQL para obtener inmuebles por comuna
    with connection.cursor as cursor
        query = """
        SELECT *
        FROM app_inmueble
        """


        cursor.execute(query)
    return 

 

if __name__ == "__main__":
    # Ruta del archivo donde se guardarán los resultados
    file_path = 'inmuebles_por_comuna.txt'
    export_inmuebles_por_comuna(file_path)
    print(f"Los inmuebles han sido exportados a {file_path}")
import os
import psycopg2
from psycopg2 import OperationalError

def get_connection():
    """
    Establece la conexión a la base de datos PostgreSQL
    usando las variables de entorno definidas en el docker-compose.
    """
    try:
        # Intentamos conectar usando las credenciales del entorno
        conn = psycopg2.connect(
            host=os.environ.get('DB_HOST', 'localhost'),
            database=os.environ.get('DB_NAME', 'hardware_store'),
            user=os.environ.get('DB_USER', 'admin'),
            password=os.environ.get('DB_PASSWORD', 'secret')
        )
        return conn
    except OperationalError as e:
        print(f"Error conectando a la BD: {e}")
        return None
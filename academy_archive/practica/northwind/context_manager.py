import os
import pyodbc 
from dotenv import load_dotenv
from contextlib import contextmanager 

# Загружаем переменные из .env файла
load_dotenv()

# Контекстный менеджер для работы с базой данных
@contextmanager
def mssql_connection(database):
    """ Контекстный менеджер """
    # Получаем значения из переменных окружения
    driver = os.getenv('DB_DRIVER')
    server = os.getenv('DB_SERVER')
    database = database
    uid = os.getenv('DB_UID')
    pwd = os.getenv('DB_PWD')

    # Устанавливаем соединение с базой данных
    conn = pyodbc.connect(
        f"DRIVER={driver};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"UID={uid};"
        f"PWD={pwd};"
    )

    try:
        yield conn
    finally:
        conn.close


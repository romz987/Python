import pandas as pd
from context_manager import mssql_connection


def test_connection():
    """ Тест соединения с базой данных """
    with mssql_connection("HospitalDB") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT @@VERSION")
        print(cursor.fetchone())


def create_database(db_name):
    """ Создаем новую базу данных """
    with mssql_connection("HospitalDB") as conn:
        cursor = conn.cursor()
        try:
            # Устанавливаем уровень изоляции на AUTOCOMMIT
            conn.autocommit = True
            cursor.execute(f"CREATE DATABASE {db_name}")
            print(f"База данных '{db_name}' успешно создана.")
        except Exception as e:
            print(f"Ошибка при создании базы данных: {e}")


def create_test_table():
    """ Создаем таблицу с указанными атрибутами """
    with mssql_connection("HelloPython") as conn:
        cursor = conn.cursor()
        try:
            # Устанавливаем уровень изоляции на AUTOCOMMIT
            conn.autocommit = True
            
            # SQL-запрос для создания таблицы
            create_table_query = """
            CREATE TABLE People (
                id INT IDENTITY(1,1) PRIMARY KEY,
                Name NVARCHAR(20) NOT NULL,
                Surname NVARCHAR(20) NOT NULL,
                Age SMALLINT NOT NULL
            )
            """
            cursor.execute(create_table_query)
            print("Таблица 'People' успешно создана.")
        except Exception as e:
            print(f"Ошибка при создании таблицы: {e}")


def insert_data_from_csv(file_path):
    """ Заполняем таблицу People данными из CSV файла """
    # Читаем данные из CSV файла
    data = pd.read_csv(file_path)

    with mssql_connection("HelloPython") as conn:
        cursor = conn.cursor()
        try:
            # Устанавливаем уровень изоляции на AUTOCOMMIT
            conn.autocommit = True
            
            # Вставляем данные в таблицу
            for index, row in data.iterrows():
                cursor.execute(
                    "INSERT INTO People (Name, Surname, Age) VALUES (?, ?, ?)",
                    row['Name'], row['Surname'], row['Age']
                )
            print("Данные успешно вставлены в таблицу 'People'.")
        except Exception as e:
            print(f"Ошибка при вставке данных: {e}")


def fetch_people():
    """ Запрашивает данные из таблицы People и возвращает их в виде списка словарей """
    with mssql_connection("HelloPython") as conn:
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM People")
            # Получаем названия столбцов
            columns = [column[0] for column in cursor.description]
            results = []
            for row in cursor.fetchall():
                # Преобразуем каждую строку в словарь
                results.append(dict(zip(columns, row)))
            return results
        except Exception as e:
            print(f"Ошибка при запросе данных: {e}")
            return []


# Пробуем
if __name__ == "__main__":
    test_connection()
    # create_database("HelloPython")
    # create_test_table()
    # insert_data_from_csv("people.csv")
    data = fetch_people()
    for _dict in data:
        for key, value in _dict.items():
            print(f"{key}: {value}")
        print()

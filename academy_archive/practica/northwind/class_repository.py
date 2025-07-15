from context_manager import mssql_connection
from class_manager_csv import CsvManager
from queries import *

class Repository:

    def __init__(
        self, 
        csv_manager: CsvManager
    ):
        """
        Конструктор класса 

        :config_manager: менеджер конфигураций
        """
        self._csvman = csv_manager


    def test_connection(self):
        """ Тест соединения """
        with mssql_connection("HospitalDB") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT @@VERSION")
            print(cursor.fetchone())


    def create_db(self, db_name: str):
        """ Создать базу данных """
        with mssql_connection("HospitalDB") as conn:
            cursor = conn.cursor()
            # Устанавливаем уровень изоляции на AUTOCOMMIT
            conn.autocommit = True
            cursor.execute(f"CREATE DATABASE {db_name}")
   

    def create_table(self, db_name: str, sql_query: str):
        """ Создать таблицу """
        # Выполняем
        with mssql_connection(db_name) as conn:
            cursor = conn.cursor()
            # Устанавливаем уровень изоляции на AUTOCOMMIT
            conn.autocommit = True
            cursor.execute(sql_query)


    def fill_customers_table(self, db_name: str, query: str):
        """ Заполнить таблицу customers_data """
        data = self._csvman.get_customers_data()
        self._fill_table(data, db_name, query)


    def fill_employees_table(self, db_name: str, query: str):
        """ Заполнить таблицу employees_data """
        data = self._csvman.get_employees_data()
        self._fill_table(data, db_name, query)


    def fill_orders_table(self, db_name: str, query: str):
        """ Заполнить таблицу orders_data """
        data = self._csvman.get_orders_data()
        self._fill_table(data, db_name, query)


    def _fill_table(self, data: list, db_name: str, query: str):
        """ Запрос на заполнение к БД """
        with mssql_connection(db_name) as conn:
            cursor = conn.cursor()
            # Устанавливаем уровень изоляции на AUTOCOMMIT
            conn.autocommit = True        
            for row in data:
                cursor.execute(query, row)

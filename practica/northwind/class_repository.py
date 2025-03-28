from context_manager import mssql_connection
from class_manager_csv import CsvManager


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
 

    def fill_customers_table(self, db_name: str):
        """ Заполнить таблицу customers_data """
        data = self._csvman.get_customers_data()
        
        with mssql_connection(db_name) as conn:
            cursor = conn.cursor()
            # Устанавливаем уровень изоляции на AUTOCOMMIT
            conn.autocommit = True
            
            for row in data:
                insert_query = "INSERT INTO users (customer_id, company_name, contact_name) VALUES (?, ?, ?)"
                cursor.execute(insert_query, row)

    def fill_employees_table(self, db_name: str):
        """ Заполнить таблицу employees_data """
        data = self._csvman.get_employees_data()
        
        with mssql_connection(db_name) as conn:
            cursor = conn.cursor()
            # Устанавливаем уровень изоляции на AUTOCOMMIT
            conn.autocommit = True
            
            for row in data:
                insert_query = "INSERT INTO employees_data (first_name, last_name, title, birth_data, notes) VALUES (?, ?, ?, ?, ?)"
                cursor.execute(insert_query, row[1:])  # Пропускаем employee_id, так как он автоинкрементный

    def fill_orders_table(self, db_name: str):
        """ Заполнить таблицу orders_data """
        data = self._csvman.get_orders_data()
        
        with mssql_connection(db_name) as conn:
            cursor = conn.cursor()
            # Устанавливаем уровень изоляции на AUTOCOMMIT
            conn.autocommit = True
            
            for row in data:
                insert_query = "INSERT INTO orders_data (customer_id, employee_id, order_date, ship_city) VALUES (?, ?, ?, ?)"
                cursor.execute(insert_query, row[1:])  # Пропускаем order_id, так как он автоинкрементный


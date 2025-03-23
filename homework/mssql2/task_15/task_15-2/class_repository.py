from context_manager import mssql_connection 
from requests import *

class RepositoryHospital:

    database = "HospitalDB"

    def test_connection(self):
        """ Тест соединения с базой данных """
        with mssql_connection(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT @@VERSION")
            print(cursor.fetchone())


    def request_exists_one(self):
        """ Первый запрос EXISTS """
        with mssql_connection(self.database) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(req_exists_one)
                return cursor.fetchone()[0]
            except Exception as e:
                print(f"error: {str(e)}")


    def request_exists_two(self):
        """ Второй запрос EXISTS """
        with mssql_connection(self.database) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(req_exists_two)
                return cursor.fetchone()[0]
            except Exception as e:
                print(f"error: {str(e)}")


    def request_any(self):
        """ Запрос ANY """
        with mssql_connection(self.database) as conn:
            cursor = conn.cursor()   
            try:
                cursor.execute(req_any)
                return cursor.fetchall()
            except Exception as e:
                print(f"error: {str(e)}")


    def request_some(self):
        """ Запрос SOME """
        with mssql_connection(self.database) as conn:
            cursor = conn.cursor()   
            try:
                cursor.execute(req_some)
                return cursor.fetchall()
            except Exception as e:
                print(f"error: {str(e)}")


    def request_all(self):
        """ Запрос ALL """
        with mssql_connection(self.database) as conn:
            cursor = conn.cursor()   
            try:
                cursor.execute(req_all)
                return cursor.fetchall()
            except Exception as e:
                print(f"error: {str(e)}")


    def request_any_all(self):
        """ Запрос ANY + ALL """
        with mssql_connection(self.database) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(req_any_all)
                return cursor.fetchall()
            except Exception as e:
                print(f"error: {str(e)}")


    def request_union(self):
        """ Запрос UNION """
        with mssql_connection(self.database) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(req_union)
                return cursor.fetchall()
            except Exception as e:
                print(f"error: {str(e)}")


    def request_union_all(self):
        """ Запрос UNION ALL"""
        with mssql_connection(self.database) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(req_union_all)
                return cursor.fetchall()
            except Exception as e:
                print(f"error: {str(e)}")


    def request_inner_join(self):
        """ Запрос UNION ALL"""
        with mssql_connection(self.database) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(req_inner_join)
                return cursor.fetchall()
            except Exception as e:
                print(f"error: {str(e)}")


    def request_left_join(self):
        """ Запрос UNION ALL"""
        with mssql_connection(self.database) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(req_left_join)
                return cursor.fetchall()
            except Exception as e:
                print(f"error: {str(e)}")


    def request_right_join(self):
        """ Запрос UNION ALL"""
        with mssql_connection(self.database) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(req_right_join)
                return cursor.fetchall()
            except Exception as e:
                print(f"error: {str(e)}")


    def request_left_right_join(self):
        """ Запрос UNION ALL"""
        with mssql_connection(self.database) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(req_left_right_join)
                return cursor.fetchall()
            except Exception as e:
                print(f"error: {str(e)}")


    def request_full_join(self):
        """ Запрос UNION ALL"""
        with mssql_connection(self.database) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(req_full_join)
                return cursor.fetchall()
            except Exception as e:
                print(f"error: {str(e)}")


# Пробуем
if __name__ == "__main__":
    repository = RepositoryHospital()

    # тест соединения
    # repository.test_connection()

    # первый запрос EXISTS 
    print("Первый запрос EXISTS:")
    print(repository.request_exists_one())
    print()

    # второй запрос EXISTS
    print("Второй запрос EXISTS:")
    print(repository.request_exists_two())
    print()

    # Запрос ANY 
    print("Запрос ANY:") 
    for i in repository.request_any():
        print(i)
    print()

    # Запрос SOME
    print("Запрос SOME:") 
    for i in repository.request_some():
        print(i)
    print()

    # Запрос ALL
    print("Запрос ALL:") 
    for i in repository.request_all():
        print(i)
    print()

    # Запрос ANY + ALL
    print("Запрос ANY + ALL:") 
    for i in repository.request_any_all():
        print(i)
    print()

    # Запрос UNION
    print("Запрос UNION:") 
    for i in repository.request_union():
        print(i)
    print()

    # Запрос UNION ALL
    print("Запрос UNION ALL:") 
    for i in repository.request_union_all():
        print(i)
    print()

    # Запрос INNER JOIN
    print("Запрос INNER JOIN:") 
    for i in repository.request_inner_join():
        print(i)
    print()

    # Запрос LEFT JOIN
    print("Запрос LEFT JOIN:") 
    for i in repository.request_left_join():
        print(i)
    print()

    # Запрос RIGHT JOIN
    print("Запрос RIGHT JOIN:") 
    for i in repository.request_right_join():
        print(i)
    print()

    # Запрос LEFT RIGHT JOIN
    print("Запрос LEFT RIGHT JOIN:") 
    for i in repository.request_left_right_join():
        print(i)
    print()

    # Запрос FULL JOIN
    print("Запрос FULL JOIN:") 
    for i in repository.request_full_join():
        print(i)
    print()

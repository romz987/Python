import os
import json
from context_manager import mssql_connection 
from requests import *

class RepositoryHospital:

    database = "HospitalDB"

    def _save_json(
        self,
        query_name: str, 
        query_result,
        filename: str
    ) -> None:
        """ 
        Сохранить результат в json  

        :param query_name: название запроса 
        :param query_result: результат выполнения запроса
        :param filename: имя json файла 

        :return: None
        """
        # Проверяем, существует ли файл
        if os.path.exists(filename):
            with open(filename, "r", encoding='utf-8') as json_file:
                try:
                    existing_data = json.load(json_file)
                except json.JSONDecodeError:
                    existing_data = {}
        else:
            existing_data = {}
        # Дополняем существующие данные новыми
        existing_data[query_name] = query_result

        with open(filename, "w", encoding='utf-8') as json_file:
            json.dump(
                existing_data, 
                json_file, 
                ensure_ascii=False, 
                default=str, 
                indent=4
            )
    

    def save_to_json_dialog(
        self, 
        query_name: str, 
        query_result,
        filename="results.json"
    ) -> str:
        """ 
        Подтверждение сохранения результатов
        в json

        :param query_name: название запроса 
        :param query_result: результат выполнения запроса
        :param filename: имя json файла 

        :return: None
        """
        try:
            user_answer = str(input(
                "Сохранить результат в json? (y/n)"
            )).lower()
            if user_answer == "y":
                self._save_json(query_name, query_result, filename)
        except Exception as e:
            print(f"error: {str(e)}")
        else:
            print(f"done!")


    def test_connection(self) -> str:
        """ Тест соединения с базой данных """
        with mssql_connection(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT @@VERSION")
            print(cursor.fetchone())


    def request_exists_one(self) -> bool:
        """ Первый запрос EXISTS """
        with mssql_connection(self.database) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(req_exists_one)
                query_result = cursor.fetchone()
                self.save_to_json_dialog(
                    "EXISTS_ONE", 
                    query_result[0]
                )
                return query_result[0]
            except Exception as e:
                print(f"error: {str(e)}")


    def request_exists_two(self) -> bool:
        """ Второй запрос EXISTS """
        with mssql_connection(self.database) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(req_exists_two)
                query_result = cursor.fetchone()
                self.save_to_json_dialog(
                    "EXISTS_TWO", 
                    query_result[0]
                )
                return query_result[0]
            except Exception as e:
                print(f"error: {str(e)}")


    def request_any(self) -> tuple:
        """ Запрос ANY """
        with mssql_connection(self.database) as conn:
            cursor = conn.cursor()   
            try:
                cursor.execute(req_any)
                query_result = cursor.fetchall()
                self.save_to_json_dialog(
                    "ANY", 
                    query_result
                )
                return query_result
            except Exception as e:
                print(f"error: {str(e)}")


    def request_some(self) -> tuple:
        """ Запрос SOME """
        with mssql_connection(self.database) as conn:
            cursor = conn.cursor()   
            try:
                cursor.execute(req_some)
                query_result = cursor.fetchall()
                self.save_to_json_dialog(
                    "SOME", 
                    query_result
                )
                return query_result
            except Exception as e:
                print(f"error: {str(e)}")


    def request_all(self) -> tuple:
        """ Запрос ALL """
        with mssql_connection(self.database) as conn:
            cursor = conn.cursor()   
            try:
                cursor.execute(req_all)
                query_result = cursor.fetchall()
                self.save_to_json_dialog(
                    "ALL", 
                    query_result
                )
                return query_result
            except Exception as e:
                print(f"error: {str(e)}")


    def request_any_all(self) -> tuple:
        """ Запрос ANY + ALL """
        with mssql_connection(self.database) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(req_any_all)
                query_result = cursor.fetchall()
                self.save_to_json_dialog(
                    "ANY+ALL", 
                    query_result
                )
                return query_result
            except Exception as e:
                print(f"error: {str(e)}")


    def request_union(self) -> tuple:
        """ Запрос UNION """
        with mssql_connection(self.database) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(req_union)
                query_result = cursor.fetchall()
                self.save_to_json_dialog(
                    "UNION", 
                    query_result
                )
                return query_result
            except Exception as e:
                print(f"error: {str(e)}")


    def request_union_all(self) -> tuple:
        """ Запрос UNION ALL """
        with mssql_connection(self.database) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(req_union_all)
                query_result = cursor.fetchall()
                self.save_to_json_dialog(
                    "UNION+ALL", 
                    query_result
                )
                return query_result
            except Exception as e:
                print(f"error: {str(e)}")


    def request_inner_join(self) -> tuple:
        """ Запрос INNER JOIN """
        with mssql_connection(self.database) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(req_inner_join)
                query_result = cursor.fetchall()
                self.save_to_json_dialog(
                    "INNER JOIN", 
                    query_result
                )
                return query_result
            except Exception as e:
                print(f"error: {str(e)}")


    def request_left_join(self) -> tuple:
        """ Запрос LEFT JOIN"""
        with mssql_connection(self.database) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(req_left_join)
                query_result = cursor.fetchall()
                self.save_to_json_dialog(
                    "LEFT JOIN", 
                    query_result
                )
                return query_result
            except Exception as e:
                print(f"error: {str(e)}")


    def request_right_join(self) -> tuple:
        """ Запрос RIGHT JOIN"""
        with mssql_connection(self.database) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(req_right_join)
                query_result = cursor.fetchall()
                self.save_to_json_dialog(
                    "RIGHT JOIN", 
                    query_result
                )
                return query_result
            except Exception as e:
                print(f"error: {str(e)}")


    def request_left_right_join(self) -> tuple:
        """ Запрос LEFT JOIN + RIGHT JOIN """
        with mssql_connection(self.database) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(req_left_right_join)
                query_result = cursor.fetchall()
                self.save_to_json_dialog(
                    "LEFT JOIN + RIGHT JOIN", 
                    query_result
                )
                return query_result
            except Exception as e:
                print(f"error: {str(e)}")


    def request_full_join(self) -> tuple:
        """ Запрос FULL JOIN """
        with mssql_connection(self.database) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(req_full_join)
                query_result = cursor.fetchall()
                self.save_to_json_dialog(
                    "FULL JOIN", 
                    query_result
                )
                return query_result
            except Exception as e:
                print(f"error: {str(e)}")




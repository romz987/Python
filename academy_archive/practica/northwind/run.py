import os
from class_builder import RepositoryBuilder 
from queries import * 


if __name__ == "__main__":
    # inst 
    repo = RepositoryBuilder.build_repository("config.json")

    # Менюшка
    while True:
        os.system("clear")
        print("БАЗА ДАННЫХ")
        print()
        print("T. Тест соединения")
        print("1. Создать базу данных")
        print()         
        print("2. Создать таблицу users")        
        print("3. Создать таблицу employees_data")        
        print("4. Создать таблицу orders_data")       
        print()         
        print("5. Заполнить таблицу users из CSV")        
        print("6. Заполнить таблицу employees_data из CSV")        
        print("7. Заполнить таблицу orders_date из CSV")
        print()
        print("0. Выход")
        print()
        # Выбор 
        choice = input("Выберите опцию: ")

        # Логика 
        match choice:
            case "T":
                try:
                    repo.test_connection()
                except Exception as e:
                    print(f"error: {str(e)}")
                finally:
                    input("нажмите любую клавишу для продолжения...")

            case "1":
                try:
                    repo.create_db("NorthWind")
                except Exception as e:
                    print(f"Ошибка при создании базы данных: {str(e)}")
                else:
                    print("База данных успешно создана!")
                finally:
                    input("нажмите любую клавишу для продолжения...")

            case "2":
                try:
                    repo.create_table("NorthWind", query_create_table_users) 
                except Exception as e:
                    print(f"error: {str(e)}")
                else:
                    print("Таблица users успешно создана!")
                finally:
                    input("нажмите любую клавишу для продолжения...")

            case "3":
                try:
                    repo.create_table("NorthWind", query_create_table_employees_data)  
                except Exception as e:
                    print(f"error: {str(e)}")
                else:
                    print("Таблица employees_data успешно создана!")
                finally:
                    input("нажмите любую клавишу для продолжения...")

            case "4":
                try:
                    repo.create_table("NorthWind", query_create_table_orders_data)  
                except Exception as e:
                    print(f"error: {str(e)}")
                else:
                    print("Таблица orders_date успешно создана!")
                finally:
                    input("нажмите любую клавишу для продолжения...")

            case "5":
                try:
                    repo.fill_customers_table("NorthWind", insert_query_customers_table)
                except Exception as e:
                    print(f"error: {str(e)}")
                else:
                    print("Таблица users успешно заполнена!")
                finally:
                    input("нажмите любую клавишу для продолжения...")

            case "6":
                try:
                    repo.fill_employees_table("NorthWind", insert_query_employees_table)
                except Exception as e:
                    print(f"error: {str(e)}")
                else:
                    print("Таблица employees_data успешно заполнена!")
                finally:
                    input("нажмите любую клавишу для продолжения...")

            case "7":
                try:
                    repo.fill_orders_table("NorthWind", insert_query_orders_table)
                except Exception as e:
                    print(f"error: {str(e)}")
                else:
                    print("Таблица orders успешно заполнена!")
                finally:
                    input("нажмите любую клавишу для продолжения...")

            case "0":
                os.system('clear')
                exit()

            case _:
                os.system('clear')
                print("Вы ввели что-то не то")
                input("нажмите любую клавишу для продолжения...")

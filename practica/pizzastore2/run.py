import os 
from class_pizzeria_builder import PizzeriaBuilder
from class_pizzeria import Pizzeria
from class_config_manager import ConfigManager
from class_orders_manager import OrdersManager
from class_pizza import Pizza
from utils import *

# Собираем пиццерию Пиццерию
config_path = "config.json"
orders_file_path = "orders.txt"
pizzeria = PizzeriaBuilder.build_pizzeria(
    config_path,
    orders_file_path,
    ConfigManager,
    OrdersManager,
    Pizzeria,
    Pizza
)


if __name__ == "__main__":

    # Запускаем меню
    while True:
        os.system('clear')
        print("ПИЦЦЕРИЯ")
        print()
        print("1. Показать ассортимент пиццы")
        print("2. Показать ассортимент топпингов")
        print("3. Заказать пиццу")
        print("4. Отчет по заказам")
        print("5. [admin] Добавить новую пиццу в меню")
        print("6. [admin] Добавить новый топпинг в меню")
        print()
        print("0. Выход")
        print("\n")
        choice = input("Выберите опцию: ")

        match choice:
            case "1":
                os.system('clear')
                try:                 
                    print("АССОРТИМЕНТ ПИЦЦЫ")
                    print()
                    show_menu_pizza(pizzeria.get_menu_pizza())

                except Exception as e:
                    print(f"Ошибка: {str(e)}")
                finally:
                    print()
                    input("Нажмите любую клавишу для продолжения...")

            case "2":
                os.system('clear')
                try:                 
                    print("АССОРТИМЕНТ ТОППИНГОВ")
                    print()
                    show_menu_toppings(pizzeria.get_menu_toppings())

                except Exception as e:
                    print(f"Ошибка: {str(e)}")
                finally:
                    print()
                    input("Нажмите любую клавишу для продолжения...")

            case "3":
                os.system('clear')
                try:                 
                    print("ЗАКАЗ ПИЦЦЫ")
                    print()
                    pizza_name = str(input(
                        "Введите название пиццы для заказа: "
                    ))
                    print()
                    toppings = str(input(
                        "Перечислите через запятую топпинги, которые вы хотите добавить: "
                    ))
                    if toppings:
                        toppings_list = [topping.strip() for topping in toppings.split(',')]
                    else:
                        toppings_list = []
                    if pizzeria.add_order(pizza_name, toppings_list) == "ok":
                        os.system("clear")
                        print(f"Вы заказали пиццу: {pizza_name}!")
                        print(f"Топпинги: {toppings_list}")
                    else:
                        print("Что-то не получилось...")

                except Exception as e:
                    print(f"Ошибка: {str(e)}")
                finally:
                    print()
                    input("Нажмите любую клавишу для продолжения...")

            case "4":
                os.system('clear')
                try:                 
                    print("ОТЧЕТ ПО ЗАКАЗАМ")
                    print()
                    summary = pizzeria.get_orders_summary()
                    if summary:
                        print(f"Всего заказано пицц: {summary["total_count"]}")
                        print(f"На общую сумму: {summary["total_profit"]}")
                    else:
                        print("Заказов нет")

                except Exception as e:
                    print(f"Ошибка: {str(e)}")
                finally:
                    print()
                    input("Нажмите любую клавишу для продолжения...")

            case "5":
                os.system('clear')
                try:                 
                    print("ДОБАВИТЬ НОВУЮ ПИЦЦУ В МЕНЮ")
                    print()
                    name = str(input("Введите название пиццы: "))
                    price = int(input("Введите стоимость пиццы: "))
                    compounds = str(input("Введите ингредиенты пиццы через запятую: "))
                    compounds_list = [ingredient.strip() for ingredient in compounds.split(',')]
                    pizzeria.add_new_pizza_to_menu(name, price, compounds_list)
                    os.system("clear")
                    print(f"Новая пицца '{name}' успешно добавлена в меню!")

                except Exception as e:
                    print(f"Ошибка: {str(e)}")
                finally:
                    print()
                    input("Нажмите любую клавишу для продолжения...")

            case "6":
                os.system('clear')
                try:                 
                    print("ДОБАВИТЬ НОВЫЙ ТОППИНГ В МЕНЮ")
                    print()
                    name = str(input("Введите название топпинга: "))
                    price = int(input("Введите стоимость топпинга: "))
                    pizzeria.add_new_topping_to_menu(name, price)
                    print()
                    print(f'Топпинг "{name}" успешно добавлен в меню')
                    print()
                except Exception as e:
                    print(f"Ошибка: {str(e)}")
                finally:
                    input("Нажмите любую клавишу для продолжения...")

            case "0":
                os.system('clear')
                exit()

            case _:
                os.system('clear')
                print("Вы нажали что-то не то...")
                input("Нажмите любую клавишу для продолжения...")


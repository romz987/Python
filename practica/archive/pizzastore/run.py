import os 
from class_pizzeria_model import PizzeriaModel
from class_pizzeria_controller import PizzeriaController
from class_pizzeria_view import PizzeriaView
from class_pizzeria_order import Order

# Инстанцируем
model = PizzeriaModel("config.json")
controller = PizzeriaController(model, Order)
view = PizzeriaView(controller)

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
                    view.show_pizza_menu()
                except Exception as e:
                    print(f"Ошибка: {str(e)}")
                finally:
                    input("Нажмите любую клавишу для продолжения...")

            case "2":
                os.system('clear')
                try:                 
                    print("АССОРТИМЕНТ ТОППИНГОВ")
                    print()
                    view.show_toppings_menu()
                except Exception as e:
                    print(f"Ошибка: {str(e)}")
                finally:
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
                    result = controller.order_pizza(pizza_name, toppings_list)
                    os.system('clear')
                    print("Вы заказали пиццу: ")
                    print(result)
                except Exception as e:
                    print(f"Ошибка: {str(e)}")
                finally:
                    input("Нажмите любую клавишу для продолжения...")

            case "4":
                os.system('clear')
                try:                 
                    print("ОТЧЕТ ПО ЗАКАЗАМ")
                    print()
                    view.show_orders_summary()
                except Exception as e:
                    print(f"Ошибка: {str(e)}")
                finally:
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
                    model.add_pizza(name, price, compounds_list)
                    print()
                    print(f'Пицца "{name}" успешно добавлена в меню')
                    print()
                except Exception as e:
                    print(f"Ошибка: {str(e)}")
                finally:
                    input("Нажмите любую клавишу для продолжения...")

            case "6":
                os.system('clear')
                try:                 
                    print("ДОБАВИТЬ НОВЫЙ ТОППИНГ В МЕНЮ")
                    print()
                    name = str(input("Введите название топпинга: "))
                    price = int(input("Введите стоимость топпинга: "))
                    model.add_topping(name, price)
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


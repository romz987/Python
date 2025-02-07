import os
from MVC_01_Model import RecipesModel
from MVC_02_Controller import RecipesController
from MVC_03_View import RecipesView 


if __name__ == "__main__":
    model = RecipesModel("data.json")
    controller = RecipesController(model)
    view = RecipesView(controller)

    # Запускаем меню
    while True:
        os.system('clear')
        print("БАЗА РЕЦЕПТОВ")
        print()
        print("1. Показать все рецепты")
        print("2. Найти рецепт по названию")
        print("3. Добавить рецепт")
        print()
        print("0. Выход")
        print("\n")
        choice = input("Выберите опцию: ")

        # Показать все рецепты
        if choice == "1":
            os.system('clear')
            try:                 
                print("ВСЕ РЕЦЕПТЫ")
                print()
                view.show_all_recipes()
            except Exception as e:
                print(f"Ошибка: {str(e)}")
            finally:
                input("Нажмите любую клавишу для продолжения...")

        # Найти рецепт по названию
        elif choice == "2":
            os.system('clear')
            try:
                print("НАЙТИ РЕЦЕПТ ПО НАЗВАНИЮ")
                print()
                name = str(input("Введите название блюда: "))
                os.system('clear')
                view.show_recipe_by_name(name.lower())
            except Exception as e:
                print(f"Ошибка: {str(e)}")
            finally:
                input("нажмите любую клавишу для продолжения...")

        # Добавить рецепт
        elif choice == "3":
            os.system('clear')
            try:
                print("ДОБАВИТЬ РЕЦЕПТ")
                print()
                recipe_name = str(input("Введите название рецепта: "))
                os.system('clear')
                author = str(input("Введите имя автора рецепта: "))
                os.system('clear')
                recipe_type = str(input("Введите тип блюда: "))
                os.system('clear')
                cuisine = str(input("К какой кухне принадлежит рецепт: "))
                os.system('clear')
                ingredients_str = str(input("Введите ингредиенты через запятую: "))
                ingredients = [ingredient.strip() for ingredient in ingredients_str.split(',')]
                os.system('clear')
                description = str(input("Напишите сам рецепт: "))
                os.system('clear')
                url = str(input("Введите ссылку на рецепт: "))
                os.system('clear')
                model.add_recipe(recipe_name, author, recipe_type, cuisine, ingredients, description, url)
            except Exception as e:
                print(f"Ошибка: {str(e)}")
            else: 
                print("Рецепт добавлен в json и сохранен!")
            finally:
                input("нажмите любую клавишу для продолжения...")

        elif choice == "0":
            print("exiting...")
            os.system('clear')
            exit()

        else:
            os.system('clear')
            print("Вы ввели что-то не то")
            input("нажмите любую клавишу для продолжения...")


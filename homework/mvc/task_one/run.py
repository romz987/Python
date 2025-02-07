import os
from MVC_01_Model import ShoesModel
from MVC_02_Controller import ShoesController
from MVC_03_View import ShoesView


if __name__ == "__main__":
    model = ShoesModel("data.json")
    controller = ShoesController(model)
    view = ShoesView(controller) 

    # Запускаем меню
    while True:
        os.system('clear')
        print("БИБЛИОТЕКА")
        print()
        print("1. Показать весь ассортимент")
        print("2. Показать ассортимент женской обуви")
        print("3. Показать ассортимент мужской обуви")
        print("4. Показать женскую обувь в наличии по размеру")
        print("5. Показать мужскую обвуь в наличии по размеру")
        print("6. Показать женскую обувь в наличии по цвету")
        print("7. Показать мужскую обувь в наличии по цвету")
        print()
        print("0. Выход")
        print("\n")
        choice = input("Выберите опцию: ")

        # Показать весь ассортмент
        if choice == "1":
            os.system('clear')
            try:                 
                print("ПОЛНЫЙ АССОРТИМЕНТ: ")
                print()
                print(view.show_all_assortment())
            except Exception as e:
                print(f"Ошибка: {str(e)}")
            finally:
                input("Нажмите любую клавишу для продолжения...")

        # Показать ассортимент женской обуви
        elif choice == "2":
            os.system('clear')
            try:
                print("АССОРТИМЕНТ ЖЕНСКОЙ ОБУВИ: ")
                print()
                print(view.show_woman_assortment())
            except Exception as e:
                print(f"Ошибка: {str(e)}")
            finally:
                input("нажмите любую клавишу для продолжения...")

        # Показать ассортимент мужской обуви
        elif choice == "3":
            os.system('clear')
            try:
                print("АССОРТИМЕНТ МУЖСКОЙ ОБУВИ: ")
                print()
                print(view.show_man_assortment())
            except Exception as e:
                print(f"Ошибка: {str(e)}")
            finally:
                input("нажмите любую клавишу для продолжения...")

        # Показать женскую обувь в наличии по размеру
        elif choice == "4":
            os.system('clear')
            try:
                searched_size = int(input("Введите искомый размер: "))
                print(f"АССОРТИМЕНТ ЖЕНСКОЙ ОБУВИ РАЗМЕРА {searched_size}: ")
                print()
                print(view.show_woman_assortment_by_size(searched_size))
            except Exception as e:
                print(f"Ошибка: {str(e)}")
            finally:
                input("нажмите любую клавишу для продолжения...")

        # Показать мужскую обвуь в наличии по размеру
        elif choice == "5":
            os.system('clear')
            try:
                searched_size = int(input("Введите искомый размер: "))
                print(f"АССОРТИМЕНТ МУЖСКОЙ ОБУВИ РАЗМЕРА {searched_size}: ")
                print()
                print(view.show_man_assortment_by_size(searched_size))
            except Exception as e:
                print(f"Ошибка: {str(e)}")
            finally:
                input("нажмите любую клавишу для продолжения...")

        # Показать женскую обувь в наличии по цвету
        elif choice == "6":
            os.system('clear')
            try:
                searched_color = str(input("Введите искомый цвет: "))
                print(f"АССОРТИМЕНТ ЖЕНСКОЙ ОБУВИ ЦВЕТА {searched_color}: ")
                print()
                print(view.show_woman_assortment_by_color(searched_color))
            except Exception as e:
                print(f"Ошибка: {str(e)}")
            finally:
                input("нажмите любую клавишу для продолжения...")

        # Показать мужскую обувь в наличии по цвету
        elif choice == "7":
            os.system('clear')
            try:
                searched_color = str(input("Введите искомый цвет: "))
                print(f"АССОРТИМЕНТ МУЖСКОЙ ОБУВИ ЦВЕТА {searched_color}: ")
                print()
                print(view.show_man_assortment_by_color(searched_color))
            except Exception as e:
                print(f"Ошибка: {str(e)}")
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


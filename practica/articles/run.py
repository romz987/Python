import os
from class_articles_model import ArticlesModel
from class_articles_controller import ArticlesController
from class_articles_view import ArticlesView 


if __name__ == "__main__":
    model = ArticlesModel("config.json")
    controller = ArticlesController(model)
    view = ArticlesView(controller)

    # Запускаем меню
    while True:
        os.system('clear')
        print("БАЗА СТАТЕЙ")
        print()
        print("1. Показать все статьи в базе")
        print("2. Найти статью по названию")
        print("3. Найти статью по имени автора")
        print("4. Добавить статью")
        print("5. Удалить статью по названию")
        print()
        print("0. Выход")
        print("\n")
        choice = input("Выберите опцию: ")

        match choice:
            case "1":
                os.system('clear')
                try:                 
                    print("ВСЕ СТАТЬИ")
                    print()
                    view.show_all_articles()
                except Exception as e:
                    print(f"Ошибка: {str(e)}")
                finally:
                    print()
                    input("Нажмите любую клавишу для продолжения...")

            case "2":
                os.system('clear')
                try:                 
                    print("ПОИСК СТАТЬИ ПО НАЗВАНИЮ")
                    print()
                    title = str(input("Введите название статьи: ")).lower()
                    os.system('clear')
                    view.show_article_by_title(title)
                except Exception as e:
                    print(f"Ошибка: {str(e)}")
                finally:
                    print()
                    input("Нажмите любую клавишу для продолжения...")

            case "3":
                os.system('clear')
                try:                 
                    print("ПОИСК СТАТЬИ ПО ИМЕНИ АВТОРА")
                    print()
                    name= str(input("Введите имя автора: ")).lower()
                    os.system('clear')
                    view.show_article_by_author(name)
                except Exception as e:
                    print(f"Ошибка: {str(e)}")
                finally:
                    print()
                    input("Нажмите любую клавишу для продолжения...")

            case "4":
                os.system('clear')
                try:                 
                    print("ДОБАВИТЬ СТАТЬЮ")
                    print()
                    title = str(input("Введите название статьи: ")).lower()
                    author = str(input("Введите имя автора: ")).lower()
                    size= str(input("Введите количество знаков в статье: "))
                    source = str(input("Где опубликована статья?: ")).lower()
                    description = str(input("Краткое описание статьи: ")).lower()
                    model.add_article(title, author, size, source, description)
                except Exception as e:
                    print(f"Ошибка: {str(e)}")
                else:
                    os.system('clear')
                    print("Статья успешно добавлена!")
                finally:
                    print()
                    input("Нажмите любую клавишу для продолжения...")

            case "5":
                os.system('clear')
                try:                 
                    print("УДАЛИТЬ СТАТЬЮ")
                    print()
                    title = str(input("Введите название статьи для удаления: ")).lower()
                    result = model.remove_article_by_title(title)
                    if result:
                        os.system('clear')
                        print("Статья успешно удалена!")
                except Exception as e:
                    print(f"Ошибка: {str(e)}")
                finally:
                    print()
                    input("Нажмите любую клавишу для продолжения...")

            case "0":
                os.system('clear')
                exit()

            case _:
                os.system('clear')
                print("Вы нажали что-то не то...")
                input("Нажмите любую клавишу для продолжения...")


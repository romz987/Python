import os 
from class_movies_model import MoviesModel
from class_movies_controller import MoviesController
from class_movies_view import MoviesView


if __name__ == "__main__":
    model = MoviesModel("config.json")
    controller = MoviesController(model)
    view = MoviesView(controller)

    # Запускаем меню
    while True:
        os.system('clear')
        print("БАЗА КИНОФИЛЬМОВ")
        print()
        print("1. Показать все фильмы в базе")
        print("2. Найти фильм по названию")
        print("3. Найти фильм по жанру")
        print("4. Добавить фильм")
        print("5. Удалить фильм по названию")
        print()
        print("0. Выход")
        print("\n")
        choice = input("Выберите опцию: ")

        match choice:
            case "1":
                os.system('clear')
                try:                 
                    print("ВСЕ ФИЛЬМЫ")
                    print()
                    view.show_all_movies()
                except Exception as e:
                    print(f"Ошибка: {str(e)}")
                finally:
                    print()
                    input("Нажмите любую клавишу для продолжения...")

            case "2":
                os.system('clear')
                try:                 
                    print("ПОИСК ФИЛЬМА ПО НАЗВАНИЮ")
                    print()
                    name = str(input("Введите название фильма: ")).lower()
                    os.system('clear')
                    view.show_movie_by_name(name)
                except Exception as e:
                    print(f"Ошибка: {str(e)}")
                finally:
                    print()
                    input("Нажмите любую клавишу для продолжения...")

            case "3":
                os.system('clear')
                try:                 
                    print("ПОИСК ФИЛЬМА ПО ЖАНРУ")
                    print()
                    genre = str(input("Введите название жанра: ")).lower()
                    os.system('clear')
                    view.show_movie_by_genre(genre)
                except Exception as e:
                    print(f"Ошибка: {str(e)}")
                finally:
                    print()
                    input("Нажмите любую клавишу для продолжения...")

            case "4":
                os.system('clear')
                try:                 
                    print("ДОБАВИТЬ ФИЛЬМ")
                    print()
                    name = str(input("Введите название фильма: ")).lower()
                    genre = str(input("Введите название жанра: ")).lower()
                    director = str(input("Введите имя режиссера: "))
                    year = str(input("Год выпуска фильма?: ")).lower()
                    duration = str(input("Введите продолжительность фильма: "))
                    studio = str(input("Какая киностудия выпустила фильм?: ")).lower()
                    actors = str(input("Перечислите актеров через запятую: ")).lower()
                    actors_list = [actor.strip() for actor in actors.split(',')]
                    model.add_movie(name, genre, director, year, duration, studio, actors)
                except Exception as e:
                    print(f"Ошибка: {str(e)}")
                else:
                    os.system('clear')
                    print("Фильм успешно добавлен!")
                finally:
                    print()
                    input("Нажмите любую клавишу для продолжения...")

            case "5":
                os.system('clear')
                try:                 
                    print("УДАЛИТЬ ФИЛЬМ")
                    print()
                    title = str(input("Введите название фильма для удаления: ")).lower()
                    result = model.remove_article_by_title(title)
                    if result:
                        os.system('clear')
                        print("Фильм успешно удален!")
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


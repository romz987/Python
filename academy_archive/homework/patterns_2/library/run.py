import os
from fabrics import ConfigManager
from fabrics import BookFactory
from fabrics import ClientFactory
from fabrics import LibraryBuilder
from class_book import Book
from class_client import Client
from class_library import Library
from logger import logger_config

logger = logger_config()


# Вспомогательные функции
# Получить список книг
def get_books_list(library: Library):
    for i in library.get_books():
        print(i)

# Получить список клиентов
def get_clients_list(library: Library):
    for i in library.get_clients():
        print(i.get_name())
    print()

# Получить спиок книг на руках у клиентов
# Получить список книг
def get_clients_books(library: Library):
    result = library.show_clients_books()
    if len(result) > 0:
        for i in result:
            print(f"Книга: {i[1]}\nНа руках у: {i[0]}" )
            print()
        return True
    else:
        print("Книг на руках нет")
        return False


if __name__ == "__main__":
    # Инстанцируем менеджер конфигурации
    config_manager = ConfigManager("config.json")

    # Инстанцируем фабричные методы для создания книг и клиентов
    books_factory = BookFactory(Book)
    clients_factory = ClientFactory(Client)

    # Инстанцируем Строителя
    library_builder = LibraryBuilder(
        Library,
        config_manager, 
        books_factory, 
        clients_factory
    )

    # Строим
    library = library_builder.build_library()


    # Запускаем меню
    while True:
        os.system('clear')
        print("БИБЛИОТЕКА")
        print()
        print("1. Показать список книг")
        print("2. Показать список клиентов")
        print("3. Взять книгу")
        print("4. Вернуть книгу")
        print("5. Информация о книге по названию")
        print("6. Показать книги на руках")
        print("7. Изменить название книги")
        print("8. [pickle] Сохранить класс в файл")
        print("9. [pickle] Загрузить класс из файла")
        print()
        print("0. Выход")
        print("\n")
        choice = input("Выберите опцию: ")

        # Показать список книг
        if choice == "1":
            os.system('clear')
            try: 
                get_books_list(library) 
            except Exception as e:
                print(f"Ошибка: {str(e)}")
                logger.error(f"run.py menu choise 1 error: {str(e)}")
            finally:
                input("Нажмите любую клавишу для продолжения...")

        # Показать список клиентов
        elif choice == "2":
            os.system('clear')
            try:
                get_clients_list(library)
            except Exception as e:
                logger.error(f"run.py menu choise 2 error: {str(e)}")
            finally:
                input("нажмите любую клавишу для продолжения...")

        # Взять книгу
        elif choice == "3":
            os.system('clear')
            try:
                for i in library.get_clients():
                    print(i.get_name())
                print()
                client_name = str(input("Введите имя клиента, который заберет книгу: "))
                print()
                get_books_list(library)
                book_name = str(input("Введите имя книги: "))
                result = library.take_book(client_name, book_name)
                if result == "done":
                    print(f"{client_name} взял книгу {book_name}")
                else:
                    print("что-то не получилось")
            except Exception as e:
                logger.error(f"run.py menu choise 3 error: {str(e)}")
            finally:
                input("нажмите любую клавишу для продолжения...")

        # Вернуть книгу
        elif choice == "4":
            os.system('clear')
            try:
                print("Книги на руках у читателей: ")
                result = get_clients_books(library)
                if result:
                    client_name = str(input(
                        "Введите имя читателя, который вернет книгу: "
                        ))
                    book_name = str(input(
                        "Введите название книги, которую вернет читатель: "
                        ))
                    library.return_book(client_name, book_name)

            except Exception as e:
                logger.error(f"run.py menu choise 4 error: {str(e)}")
            finally:
                input("нажмите любую клавишу для продолжения...")

        # Информация о книге по названию
        elif choice == "5":
            os.system('clear')
            try:
                book_name = str(input("Введите название книги: "))
                print(library.search_book(book_name))
            except Exception as e:
                logger.error(f"run.py menu choise 5 error: {str(e)}")
            finally:
                input("нажмите любую клавишу для продолжения...")

        # Показать книги на руках
        elif choice == "6":
            os.system('clear')
            try:
                get_clients_books(library)
            except Exception as e:
                logger.error(f"run.py menu choise 6 error: {str(e)}")
            finally:
                input("нажмите любую клавишу для продолжения...")

        # Изменить название книги
        elif choice == "7":
            os.system('clear')
            try:
                current_book_name = str(input("Введите старове название книги: "))
                new_book_name = str(input("Введите новое название книги: "))
                if library.change_book_title(current_book_name, new_book_name) == "invalid book name":
                    print("Не удалось найти книгу с таким названием")
                else:
                    print("Название измненено")
            except Exception as e:
                logger.error(f"run.py menu choise 7 error: {str(e)}")
            finally:
                input("нажмите любую клавишу для продолжения...")

        # Сохранить класс в файл
        elif choice == "8":
            os.system('clear')
            try:
                Library.pickle_class(library)
            except Exception as e:
                logger.error(f"run.py menu choise 8 error: {str(e)}")
            finally:
                logger.info("saving libabry state to pkl file...")
                print("Состояние библиотеки сохранено в файл")
                print()
                input("нажмите любую клавишу для продолжения...")

        # Загрузить класс из файла
        elif choice == "9":
            os.system('clear')
            try:
                library = Library.unpicke_class()
            except Exception as e:
                logger.error(f"run.py menu choise 9 error: {str(e)}")
            finally:
                logger.info("libabry deployed from pkl file...")
                print("Библиотека развернута из сохраненного файла")
                print()
                input("нажмите любую клавишу для продолжения...")

        elif choice == "0":
            logger.info("exiting...")
            os.system('clear')
            exit()

        else:
            logger.info("run.py menu wrong choise")
            os.system('clear')
            print("Вы ввели что-то не то")
            input("нажмите любую клавишу для продолжения...")


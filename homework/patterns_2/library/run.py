import os
from class_library_builder import LibraryBuilder
from class_library import Library
from class_book import Book


books_list = [
    ["Три товарища", "Эрих Мария Ремарк", "1936"],
    ["Цветы для Элджернона", "Дэниел Киз", "1959"],
    ["Вино из одуванчиков", "Рей Бредберри", "1957"],
    ["Алиса в стране чудес", "Льюис Кэролл", "1865"],
    ["Бронированное место", "Бронированное место", "1932"]
]


if __name__ == "__main__":
    lib_builder = LibraryBuilder(Library, Book)
    library = lib_builder.build_library(books_list)

    while True:
        os.system('clear')
        print("Библиотека")
        print("1. Показать список книг")
        print("2. Изменить название книги")
        print("3. Добавить книгу")
        print("4. Удалить книгу")
        print("0. Выход")
        print("\n")
        choice = input("Выберите опцию: ")

        if choice == "1":
            os.system('clear')
            try: 
                books = library.get_all_books()
                for book in books:
                    print(book)
                    print()
            except Exception as e:
                print(f"Ошибка: {str(e)}")
            finally:
                input("Нажмите любую клавишу для продолжения...")

        elif choice == "2":
            os.system('clear')
            try: 
                pass
            except Exception as e:
                print(f"Ошибка: {str(e)}")
            finally:
                input("Нажмите любую клавишу для продолжения...")

        elif choice == "3":
            os.system('clear')
            try: 
                pass
            except Exception as e:
                print(f"Ошибка: {str(e)}")
            finally:
                input("Нажмите любую клавишу для продолжения...")

        elif choice == "4":
            os.system('clear')
            try: 
                pass
            except Exception as e:
                print(f"Ошибка: {str(e)}")
            finally:
                input("Нажмите любую клавишу для продолжения...")

        elif choice == "0":
            os.system('clear')
            exit()

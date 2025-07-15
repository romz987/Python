# НЕ РУГАЙТЕ МЕНЯ Я В ПРОЦЕССЕ!
import os
from abstracts import (
    BookBase,
    LibraryBase
)


books_list = [
    ["Три товарища", "Эрих Мария Ремарк", "1936"],
    ["Цветы для Элджернона", "Дэниел Киз", "1959"],
    ["Вино из одуванчиков", "Рей Бредберри", "1957"],
    ["Алиса в стране чудес", "Льюис Кэролл", "1865"],
    ["Бронированное место", "Бронированное место", "1932"]
]


class Book(BookBase):

    def __init__(
        self,
        title: str,
        author: str,
        year: str,
        availible=True,
        holder="библиотека"
    ):
        self.title = title
        self.author = author
        self.year = year
        self.availible = availible
        self.holder = holder

    def get_title(self) -> str:
        """ Вернуть название книги """
        return self.title

    def set_title(self, new_title: str) -> None:
        """ Вернуть название книги """
        self.title = new_title

    def __str__(self) -> str:
        """ Вывести данные о книге """
        if self.availible:
            status = "доступна"
        else:
            status = "на руках"
        answer = (
            f"Книга {self.title} автора {self.author} {self.year} года.\n"
            f"Доступность: {status}. Находится: {self.holder}"
        )
        return answer

    def change_availability(self, status: bool) -> None:
        """ Изменить статус книги """
        if status is True:
            self.availible = True
        else:
            self.availible = False

    def change_holder(self, holder_name) -> None:
        """ Изменить имя держателя книги"""
        self.holder = holder_name


class LibraryBuilder:
    """ Строитель библиотеки """

    def __init__(self, books_list: list):
        self.books_list = books_list
        self.books = []
        for i in self.books_list:
            book = Book(i[0], i[1], i[2])
            self.books.append(book)

    def build(self):
        return Library(self.books)


class Library():

    def __init__(self, books: list):
        self.books = books

    def get_all_books(self) -> list:
        """ Вернуть описание всех книг """
        books = []
        for i in self.books:
            books.append(i.__str__())
        return books

    def add_new_book(self, title: str, author: str, year: str):
        """ Добавить новую книгу """
        book = Book(title, author, year)
        self.books.append(book)

    def change_book_title(self, current_book_title: str, new_book_title: str) -> bool:
        """ Изменить текущую книгу """
        for book in self.books:
            if book.get_title() == current_book_title:
                book.set_title(new_book_title)
                return True
        return False

    def remove_book(self, book_title: str) -> bool:
        """ Удалить книгу из коллекции """
        for book in self.books:
            if book.get_title() == book_title:
                self.books.remove(book)
                return True
        return False

    def search_book(self, book_title: str) -> bool:
        """ Найти книгу в коллекции """
        for book in self.books:
            if book.get_title() == book_title:
                return True
        return False

    def give_book(self, book: str):
        """ Отдать книгу библиотекарю """
        pass

    def receive_book(self, book: str):
        """ Получить книгу от библиотекаря """
        pass


if __name__ == "__main__":
    builder = LibraryBuilder(books_list)
    library = builder.build()
    print(library.books)

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
            books = library.get_all_books()
            for book in books:
                print(book)
                print()
            input("Нажмите любую клавишу для продолжения...")

        elif choice == "2":
            os.system('clear')
            old_book_title = str(input("Введите текущее название книги: "))
            new_book_title = str(input("Введите новое название книги: "))

            if library.change_book_title(old_book_title, new_book_title):
                print(
                    f"Название книги {old_book_title} изменено на {new_book_title}"
                )
            else:
                print(f"Книга {old_book_title} не найдена")
            input("Нажмите любую клавишу для продолжения...")

        elif choice == "3":
            os.system('clear')
            title = str(input("Введите название книги: "))
            author = str(input("Введите имя автора книги: "))
            year = str(input("Введите год издания: "))
            library.add_new_book(title, author, year)
            input("Нажмите любую клавишу для продолжения...")

        elif choice == "4":
            os.system('clear')
            book_title = str(input("Введите название книги: "))
            library.remove_book(book_title)
            print(f"Книга {book_title} удалена из библиотеки")
            input("Нажмите любую клавишу для продолжения...")

        elif choice == "0":
            print("Завершение работы программы...")
            os.system('clear')
            exit()

        else: 
            os.system('clear')
            print("Вы что то не то ввели")
            input("Нажмите любую клавишу для продолжения...")



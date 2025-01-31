from abstracts import LibraryBase


class Library(LibraryBase):

    def __init__(self, books: list):
        self.books = books

    def get_all_books(self) -> list:
        """ Вернуть описание всех книг """
        books = []
        for i in self.books:
            books.append(i.__str__())
        return books

    def add_new_book(self, title: str, author: str, year: str) -> None:
        """ 
        Добавить новую книгу 
        
        :param title: Название книги
        :param author: Автор книги
        :param year: Год публикации
        :return: None
        """
        book = Book(title, author, year)
        self.books.append(book)

    def change_book_title(self, current_book_title: str, new_book_title: str) -> bool:
        """ 
        Изменить текущую книгу 

        :param current_book_title: Текущее название книги
        :param new_book_title: Новое название книги
        :return: Bool
        """
        for book in self.books:
            if book.get_title() == current_book_title:
                book.set_title(new_book_title)
                return True
        return False

    def remove_book(self, book_title: str) -> bool:
        """ 
        Удалить книгу из коллекции 

        :param new_book_title: Новое название книги
        :return: Bool
        """
        for book in self.books:
            if book.get_title() == book_title:
                self.books.remove(book)
                return True
        return False

    def search_book(self, book_title: str) -> str:
        """ 
        Найти книгу в коллекции по названию

        :param new_book_title: Новое название книги
        :return: Информация о книге
        """
        for book in self.books:
            if book.get_title() == book_title:
                return book.__str__()

    def give_book(self, book: str):
        """ Отдать книгу библиотекарю """
        pass

    def receive_book(self, book: str):
        """ Получить книгу от библиотекаря """
        pass



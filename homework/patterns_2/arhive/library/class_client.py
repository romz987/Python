from class_request import LibraryRequest


class Client:


    def __init__(self, name: str):
        self.name = name
        self.books = []

    def take_book(self, book_name: str) -> None:
        """Взять книгу в библиотеке """
        book_request = LibraryRequest(book_name, self.name)

    def return_book(self):
        """Вернуть книгу в библиотеку """
        pass

    def get_client_books(self):
        """ Показать книги на руках """
        pass

    def get_name(self):
        return self.name

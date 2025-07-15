import pickle
import json
from logger import logger_config

logger = logger_config()

class Library:


    def __init__(self, books: list, clients: list):
        self._books = books
        self._clients = clients

    def get_books(self):
        logger.info("get books request")
        return self._books

    def get_clients(self):
        logger.info("get clients request")
        return self._clients

    def search_book(self, book_name: str):
        """ Найти книгу по названию """
        logger.info(f"search books request. book name: {book_name}")
        for i in self._books:
            if i.title == book_name:
                logger.info("book found")
                return i
        logger.info("book not found")
        return "invalid book name"

    def change_book_title(self, current_book_name: str, new_book_name: str):
        """ Изменить название книги """
        logger.info(
            f"change book name request from {current_book_name} to {new_book_name}"
        )
        book = self.search_book(current_book_name)
        if book != "invalid book name":
            book.title = new_book_name
            logger.info("book name changed")
            return "title changed"
        else:
            logger.info("book name unchanged")
            return book

    def take_book(self, client_name: str, book_name: str):
        """ Взять книгу """
        logger.info(f"take book named: {book_name} request from: {client_name}")
        for i in self._clients:
            if i.get_name() == client_name:
                client = i

        if client is None:
            logger.info(f"client: {client_name} not found")
            return "Client not found"

        for i in self._books:
            if i.title == book_name:
                book = i

        if book is None:
            logger.info(f"book: {book_name} not found")
            return "Book not found"        

        self._books.remove(book)
        client._books.append(book)
        logger.info("book taken")
        return "done"

    def return_book(self, client_name: str, book_name: str):
        """ Вернуть книгу в библиотеку"""
        logger.info(
            f"return book named: {book_name} from client: {client_name} request"
        )
        for i in self._clients:
            if i.get_name() == client_name:
                client = i
                for b in i._books:
                    if b.title == book_name:
                        i._books.remove(b)
                        self._books.append(b)
                        logger.info("book returned")
                        return True
        logger.info(f"error occured while book returning")
        return False

    def show_clients_books(self) -> list:
        """ Показать книги на руках у клиентов """
        logger.info("show client books request")
        result = []
        for i in self._clients:
            # print(len(i._books))
            if len(i._books) > 0:
                client_name = i.get_name()
                # print(i._books)
                for b in i._books:
                    book_name = b.title
                    result.append([client_name, book_name])
        return result

    @staticmethod
    def pickle_class(library, file_name="library_data.pkl") -> None:
        """ Сохарнить экземпляр в файл """
        with open(file_name, "wb") as file:
            pickle.dump(library, file)

    @staticmethod
    def unpicke_class(file_path="library_data.pkl"):
        """ Загрузить класс из файла """
        with open(file_path, "rb") as file:
            result = pickle.load(file)
            return result

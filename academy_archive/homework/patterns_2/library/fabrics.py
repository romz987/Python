import json
from class_book import Book
from class_client import Client
from class_library import Library
from logger import logger_config

logger = logger_config()


class ConfigManager:

    def __init__(self, config_path):
        try:
            self._load_config(config_path)
        except Exception:
            raise
        else: 
            logger.info("configmanager: config file loaded")

    def _load_config(self, config_path):
        """ Загрузить конфиг """
        with open(config_path, "r", encoding="UTF-8") as json_file:
            self._config = json.load(json_file)

    def get_books(self):
        """ Получить список книг из конфига """
        logger.info("configmanager: request books from config")
        return self._config["books"]
          
    def get_clients(self):
        """ Получить список клиентов из конфига """
        logger.info("configmanager: request clients from config")
        return self._config["clients"]


class ClientFactory:

    def __init__(self, Client: type):
        self._Client = Client

    def create_client(self, name: str):
        """ 
        Фабричный метод 
        Создаем объект клента
        """
        return self._Client(name)


class BookFactory:

    def __init__(self, Book: type):
        self._Book = Book

    def create_book(self, book: list):
        """ 
        Фабричный метод 
        Создаем объект книги
        """
        return self._Book(book[0], book[1], book[2])


class LibraryBuilder:

    def __init__(
            self,
            class_library: type,
            config_manager: ConfigManager, 
            books_factory: BookFactory, 
            clients_factory: ClientFactory
    ):  
        self._Library = class_library
        self._config_manager = config_manager
        self._books_factory = books_factory
        self._clients_factory = clients_factory
        self._books = []
        self._clients = []

    def build_library(self):
        """ Построить библиотеку """
        books = self._config_manager.get_books()
        clients = self._config_manager.get_clients()
        # Книги 
        books_list = self.create_books_list(books)
        for i in books_list:
            book = self._books_factory.create_book(i)
            self._books.append(book)
        # Клиенты
        for i in clients:
            client = self._clients_factory.create_client(i)
            self._clients.append(client)
        # Строим библиотеку
        library = self._Library(self._books, self._clients)
        logger.info("librarybuilder: library builded!")
        return library

    def create_books_list(self, books: dict):
        """ Получить список книг из конфига """
        books_list = []
        for key, value in books.items():
            book = []
            book.append(key)
            for i in value:
                book.append(i)
            books_list.append(book)
        return books_list

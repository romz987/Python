from class_library import Library
from class_book import Book
from class_client import Client
from abstracts import LibraryBuilderBase


class LibraryBuilder(LibraryBuilderBase):
    """ Строитель библиотеки """


    def __init__(self, class_library: type, class_book: type, class_client: type):
        self.class_library = class_library
        self.class_book = class_book
        self.class_client = class_client


    def build_library(self, books_list: list, clients_list: list) -> Library:
        """ 
        Строитель класса библиотеки 

        :param books_list: Список книг
        :return: Экземплер класса библиотеки
        """
        books = []
        clients = []
        for i in books_list:
            book = self.class_book(i[0], i[1], i[2])
            books.append(book)
        for i in clients_list:
            client = self.class_client(i)
            clients.append(client)
        return self.class_library(books, clients, self.class_book)


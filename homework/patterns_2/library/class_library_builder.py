from class_library import Library
from class_book import Book
from abstracts import LibraryBuilderBase


class LibraryBuilder(LibraryBuilderBase):
    """ Строитель библиотеки """


    def __init__(self, class_library: type, class_book: type):
        self.class_library = class_library
        self.class_book = class_book


    def build_library(self, books_list: list) -> Library:
        """ 
        Строитель класса библиотеки 

        :param books_list: Список книг
        :return: Экземплер класса библиотеки
        """
        books = []
        for i in books_list:
            book = self.class_book(i[0], i[1], i[2])
            books.append(book)
        return self.class_library(books, self.class_book)


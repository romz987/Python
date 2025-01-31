from class_library import Library
from class_book import Book
from abstracts import LibraryBuilderBase


class LibraryBuilder(LibraryBuilderBase):
    """ Строитель библиотеки """


    def __init__(self, library_class: type, book_class: type):
        self.library_class = library_class
        self.book_class = book_class


    def build_library(self, books_list: list) -> Library:
        """ 
        Строитель класса библиотеки 

        :param books_list: Список книг
        :return: Экземплер класса библиотеки
        """
        books = []
        for i in books_list:
            book = self.book_class(i[0], i[1], i[2])
            books.append(book)
        return self.library_class(books)


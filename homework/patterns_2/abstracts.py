from abc import ABC, abstractmethod


class BookBase(ABC):

    @abstractmethod
    def __init__(
        self,
        title: str,
        author: str,
        year: str,
        availible: str,
        holder: str
    ):
        pass

    @abstractmethod 
    def __str__(self):
        pass

    @abstractmethod
    def change_availability(self):
        """ Изменить статус книги """
        pass

    @abstractmethod 
    def change_holder(self):
        """ Изменить имя держателя книги"""
        pass


class LibraryClientBase(ABC):

    @abstractmethod
    def __init__(self, name: str):
        pass

    @abstractmethod 
    def take_book(self):
        """ Взять книгу """
        pass

    @abstractmethod 
    def return_book(self):
        """ Вернуть книгу """
        pass


class LibraryBase(ABC):

    @abstractmethod
    def __init__(self, books: list):
        pass

    @abstractmethod 
    def add_new_book(self, book: str):
        """ Добавить новую книгу """
        pass

    @abstractmethod 
    def change_book_data(self, book: str):
        """ Изменить текущую книгу """
        pass

    @abstractmethod 
    def remove_book(self, book: str):
        """ Удалить книгу из коллекции """
        pass

    @abstractmethod 
    def search_book(self, book: str):
        """ Найти книгу в коллекции """
        pass

    @abstractmethod 
    def give_book(self, book: str):
        """ Отдать книгу библиотекарю """
        pass

    @abstractmethod 
    def receive_book(self, book: str):
        """ Получить книгу от библиотекаря """
        pass


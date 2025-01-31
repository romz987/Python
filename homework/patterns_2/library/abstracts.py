from abc import ABC, abstractmethod 


class LibraryBase(ABC):
    """ Базовый класс библиотеки """

    @abstractmethod 
    def __init__(self, books: list):
        pass

    @abstractmethod 
    def get_all_books(self) -> list:
        """ Вернуть описание всех книг """
        pass

    @abstractmethod 
    def add_new_book(self, title: str, author: str, year: str) -> None:
        """ Добавить новую книгу """
        pass

    @abstractmethod 
    def change_book_title(self, current_book_title: str, new_book_title: str) -> bool:
        """ Изменить текущую книгу """
        pass

    @abstractmethod 
    def remove_book(self, book_title: str) -> bool:
        """ Удалить книгу из коллекции """
        pass

    @abstractmethod 
    def search_book(self, book_title: str) -> str:
        """ Найти книгу в коллекции по названию """
        pass

    @abstractmethod 
    def give_book(self, book: str):
        """ Отдать книгу библиотекарю """
        pass

    @abstractmethod 
    def receive_book(self, book: str):
        """ Получить книгу от библиотекаря """
        pass


class BookBase(ABC):
    """ Базовый класс книги """

    @abstractmethod 
    def __init__(
        self,
        title: str,
        author: str,
        year: str,
        available=True,
        holder="библиотека"
    ):
        pass

    @abstractmethod 
    def title(self) -> str:
        """ Вернуть название книги """
        pass

    @abstractmethod 
    def title(self, new_title: str) -> None:
        """ Изменить название книги """
        pass

    @abstractmethod 
    def available(self) -> bool:
        """ Вернуть статус книги """
        pass

    @abstractmethod 
    def available(self, status: bool) -> None:
        """ Установить статус книги """
        pass

    @abstractmethod 
    def holder(self) -> str:
        """ Вернуть имя держателя книги """
        pass

    @abstractmethod 
    def holder(self, holder_name: str) -> None:
        """ Изменить имя держателя книги """
        pass

    @abstractmethod 
    def __str__(self) -> str:
        """ Вывести данные о книге """
        pass


class LibraryBuilderBase(ABC):
    """ Базовый класс строитель библиотеки """

    @abstractmethod 
    def __init__(self, library_class: type, book_class: type):
        pass

    @abstractmethod 
    def build_library(self, books_list: list):
        """ Строитель класса библиотеки """
        pass

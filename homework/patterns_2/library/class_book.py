from abstracts import BookBase


class Book(BookBase):

    def __init__(
        self,
        title: str,
        author: str,
        year: str,
        available=True,
        holder="библиотека"
    ):
        self._title = title
        self._author = author
        self._year = year
        self._available = available
        self._holder = holder

    @property
    def title(self) -> str:
        """ Вернуть название книги """
        return self._title

    @title.setter
    def title(self, new_title: str) -> None:
        """ Изменить название книги """
        self._title = new_title

    @property
    def available(self) -> bool:
        """ Вернуть статус книги """
        return self._available

    @available.setter
    def available(self, status: bool) -> None:
        """ Установить статус книги """
        if not isinstance(status, bool):
            raise ValueError("Значение может быть только булевым")
        self._available = status

    @property
    def holder(self) -> str:
        """ Вернуть имя держателя книги """
        return self._holder

    @holder.setter
    def holder(self, holder_name: str) -> None:
        """ Изменить имя держателя книги """
        self._holder = holder_name

    def __str__(self) -> str:
        """ Вывести данные о книге """
        status = "доступна" if self._available else "на руках"
        answer = (
            f"Книга {self._title} автора {self._author} {self._year} года.\n"
            f"Доступность: {status}. Находится: {self._holder}"
        )
        return answer


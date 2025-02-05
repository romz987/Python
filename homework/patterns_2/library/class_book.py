class Book:

    def __init__(
        self,
        title: str,
        author: str,
        year: str,
    ):
        self._title = title
        self._author = author
        self._year = year

    @property
    def title(self) -> str:
        """ Вернуть название книги """
        return self._title

    @title.setter
    def title(self, new_title: str) -> None:
        """ Изменить название книги """
        self._title = new_title

    def __str__(self) -> str:
        """ Вывести данные о книге """
        answer = (
            f'Книга: "{self._title}"\nАвтор: {self._author}. Год публикации: {self._year}.\n'
        )
        return answer

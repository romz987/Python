from class_movies_controller import MoviesController 


class MoviesView:

    def __init__(self, controller: MoviesController):
        self._controller = controller 

    def show_all_movies(self) -> None:
        """ Показать все доступные фильмы """
        data = self._controller.get_all_movies()
        self.__show_movie(data)

    def show_movie_by_name(self, name: str) -> None:
        """ Найти фильм по названию """
        data = self._controller.get_movie_by_name(name)
        if data:
            self.__show_movie(data)
        else:
            print(f"Не удалось найти фильм '{name}'")

    def show_movie_by_genre(self, genre: str) -> None:
        """ Найти фильмы по жанру """
        data = self._controller.get_movie_by_genre(genre)
        if data:
            self.__show_movie(data)
        else:
            print(f"Не удалось найти фильм жанра '{genre}'")

    def __show_movie(self, data: dict) -> None:
        """ Вывод фильма на экран """
        for name, metadata in data.items():
            print(f"Фильм: {name.upper()}")
            print(f"Жанр: {metadata["genre"]}")
            print(f"Режиссер: {metadata["director"]}")
            print(f"Год выпуска: {metadata["year"]}")
            print(f"Продолжительность: {metadata["duration"]}")
            print(f"Студия: {metadata["studio"]}")
            print(f"Актеры: {metadata["actors"]}")
            print()


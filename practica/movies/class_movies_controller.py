from class_movies_model import MoviesModel


class MoviesController:

    def __init__(self, model: MoviesModel):
        self._model = model

    def get_all_movies(self) -> dict:
        """ Возвращает все фильмы """
        pass

    def get_movie_by_name(self, name: str) -> dict:
        """ Возвращает фильм по названию """
        pass

    def get_movie_by_genre(self, name: str) -> dict:
        """ Возвращает фильм по имени автора """
        pass

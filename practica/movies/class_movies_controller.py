from class_movies_model import MoviesModel


class MoviesController:

    def __init__(self, model: MoviesModel):
        self._model = model

    def get_all_movies(self) -> dict:
        """ Возвращает все фильмы """
        return self._model.get_movies()

    def get_movie_by_name(self, searched_name: str) -> dict:
        """ Возвращает фильм по названию """
        data = self.get_all_movies()
        for name, metadata in data.items():
            if name.lower() == searched_name:
                result = {}
                result[name] = metadata
                return result 
        return False

    def get_movie_by_genre(self, searched_genre: str) -> dict:
        """ Возвращает фильм по имени автора """
        data = self.get_all_movies()
        for name, metadata in data.items():
            if metadata["genre"].lower() == searched_genre:
                result = {}
                result[name] = metadata
                return result 
        return False

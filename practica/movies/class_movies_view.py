from class_movies_controller import MoviesController 


class MoviesView:

    def __init__(self, controller: MoviesController):
        self._controller = controller 

    def show_all_movies(self) -> None:
        """ Показать все доступные фильмы """
        pass 

    def show_movies_by_name(self, name: str) -> None:
        """ Найти фильм по названию """
        pass 

    def show_movies_by_genre(self, name: str) -> None:
        """ Найти фильмы по жанру """
        pass

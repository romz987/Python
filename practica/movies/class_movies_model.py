import json 


class MoviesModel:

    def __init__(self, config_path: str):
        self._config_path = config_path

    def _load_config(self) -> dict:
        """ Загрузить конфинг """
        pass

    def _save_config(self) -> None:
        """ Сохранить конфиг """
        pass

    def get_movies(self) -> dict:
        """ Возвращает все фильмы """
        pass

    def add_movie(self) -> None:
        """ Добавить фильм """
        pass 

    def remove_movie(self) -> None:
        """ Удалить фильм """
        pass

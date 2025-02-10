import json 


class MoviesModel:

    def __init__(self, config_path: str):
        self._config_path = config_path
        try:
            self._config = self._load_config()
        except Exception as e:
            raise

    def _load_config(self) -> dict:
        with open(self._config_path, "r", encoding="utf-8") as file:
            config = json.load(file)
        return config

    def _save_config(self) -> None:
        """ Сохранить конфиг """
        with open(self._config_path, "w", encoding="utf-8") as file:
            json.dump(self._config, file, ensure_ascii=False, indent=2)

    def get_movies(self) -> dict:
        """ Возвращает все фильмы """
        return self._config 

    def add_movie(
        self,
        name: str,
        genre: str,
        director: str,
        year: str,
        duration: str,
        studio: str,
        actors: list
    ) -> None:
        """ Добавить фильм """
        new_movie = {
            "genre": genre,            
            "director": director,            
            "year": year,            
            "duration": duration,            
            "studio": studio,            
            "actors": actors,            
        }
        self._config[name] = new_movie
        self._save_config()

    def remove_movie(self, movie_name: str) -> None:
        """ Удалить фильм """
        try:
            self._config.pop(movie_name)
        except Exception as e:
            print(f"error: {str(e)}")
            return False
        else:
            self._save_config()
            return True

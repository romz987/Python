import json 


class ArticlesModel:

    def __init__(self, config_path: str):
        self._config_path = config_path
        try:
            self._config = self._load_config()
        except Exception as e:
            raise

    def _load_config(self) -> dict:
        """ Загрузить конфинг """
        with open(self._config_path, "r", encoding="utf-8") as file:
            config = json.load(file)
        return config
    
    def _save_config(self) -> None:
        """ Сохранить конфиг """
        with open(self._config_path, "w", encoding="utf-8") as file:
            json.dump(self._config, file, ensure_ascii=False, indent=2)

    def get_articles(self) -> dict:
        """ Возвращает все статьи """
        return self._config 

    def add_article(
        self,
        title: str,
        author: str,
        size: str,
        source: str,
        description: str
    ) -> None:
        """ Добавить статью """
        new_article = {
            "автор": author,
            "количество знаков": size,
            "опубликована": source,
            "краткое описание": description
        }
        self._config[title] = new_article
        self._save_config()

    def remove_article_by_title(self, searched_title: str) -> bool:
        """ Удалить статью по названию """
        try:
            self._config.pop(searched_title)
        except Exception as e:
            print(f"error: {str(e)}")
            return False
        else:
            self._save_config()
            return True

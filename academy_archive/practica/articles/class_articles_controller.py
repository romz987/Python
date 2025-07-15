from class_articles_model import ArticlesModel


class ArticlesController:

    def __init__(self, model: ArticlesModel):
        self._model = model

    def get_all_articles(self) -> dict:
        """ Возвращает все статьи """
        return self._model.get_articles()

    def get_article_by_title(self, searched_title: str) -> dict:
        """ Возвращает статью по названию """
        data = self.get_all_articles()
        for title, metadata in data.items():
            if title == searched_title:
                result = {}
                result[title] = metadata
                return result
        return False
            
    def get_article_by_author(self, name: str) -> dict:
        """ Возвращает статью по имени автора """
        data = self.get_all_articles()
        result = {}
        for title, metadata in data.items():
            if metadata["автор"] == name:
                result = {}
                result[title] = metadata
                return result
        return False


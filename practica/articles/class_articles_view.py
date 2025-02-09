from class_articles_controller import ArticlesController 


class ArticlesView:

    def __init__(self, controller: ArticlesController):
        self._controller = controller

    def __show_article(self, data: dict) -> None:
        """ Вывод статьи на экран """
        for title, metadata in data.items():
            print(f"Статья: {title.upper()}")
            print(f"Автор: {metadata["автор"]}")
            print(f"Количество знаков: {metadata["количество знаков"]}")
            print(f"Источник: {metadata["опубликована"]}")
            print(f"Краткое содержание: {metadata["краткое описание"]}")
            print()

    def show_all_articles(self) -> None:
        """ Показать все статьи """
        data = self._controller.get_all_articles()
        self.__show_article(data)   

    def show_article_by_title(self, title: str) -> None:
        """ Показать статью по названию """
        data = self._controller.get_article_by_title(title)
        if data:
            self.__show_article(data)
        else:
            print()
            print("Статья не найдена")

    def show_article_by_author(self, name: str) -> None:
        """ Показать статью по имени автора """
        data = self._controller.get_article_by_author(name)
        if data:
            self.__show_article(data)
        else:
            print()
            print("Статья не найдена")

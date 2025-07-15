from MVC_01_Model import RecipesModel
from MVC_02_Controller import RecipesController 


class RecipesView:

    def __init__(self, controller: RecipesController):
        self._controller = controller 

    def show_all_recipes(self):
        """ Показать все рецепты """
        data = self._controller.get_all_recipes()
        for recipe, content in data.items():
            print(f"Блюдо: {recipe.capitalize()}")
            print(f"Ссылка: {content["url"]}")
            print(f"Автор: {content["автор"]}")
            print(f"Кухня: {content["кухня"]}")
            print(f"Тип рецепта: {content["тип рецепта"]}")
            print(f"Ингредиенты: {content["ингредиенты"]}")
            print(f"Рецепт: {content["описание"]}")
            print()

    def show_recipe_by_name(self, name: str):
        """ Найти рецепт по названию рецепта """
        data = self._controller.get_recipe_by_name(name)
        for recipe, content in data.items():
            print(f"Блюдо: {recipe.capitalize()}")
            print(f"Ссылка: {content["url"]}")
            print(f"Автор: {content["автор"]}")
            print(f"Кухня: {content["кухня"]}")
            print(f"Тип рецепта: {content["тип рецепта"]}")
            print(f"Ингредиенты: {content["ингредиенты"]}")
            print(f"Рецепт: {content["описание"]}")
            print()


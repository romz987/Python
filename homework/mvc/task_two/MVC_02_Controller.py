from MVC_01_Model import RecipesModel


class RecipesController:


    def __init__(self, model: RecipesModel):
        self._model = model

    def get_all_recipes(self):
        """ забрать из модели все рецепты """
        data = self._model.get_recipes()
        return data

    def get_recipe_by_name(self, name: str):
        """ вернуть рецепт по названию """
        all_recipes = self.get_all_recipes()
        result = {}
        for key, value in all_recipes.items():
            if key == name:
                result[key] = value
                return result
        return False

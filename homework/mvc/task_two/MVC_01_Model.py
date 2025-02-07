import json


class RecipesModel:

    def __init__(self, recipes_json_path: str):
        self.recipes_json_path = recipes_json_path
        try: 
            self._recipes_json = self._load_file()
        except Exception:
            raise

    def _load_file(self):
        """ Загрузка файла """
        with open(self.recipes_json_path, "r", encoding="UTF-8") as file:
            data = json.load(file)
        return data

    def _save_file(self):
        """ Сохранение файла """
        with open(self.recipes_json_path, "w", encoding="UTF-8") as file:
            json.dump(self._recipes_json, file, ensure_ascii=False, indent=2)

    def get_recipes(self):
        """ Получить весь доступный ассортимент """
        return self._recipes_json

    def add_recipe(
        self,
        recipe_name: str,
        author: str,
        recipe_type: str,
        cuisine: str,
        ingredients: list,
        description: str,
        url: str
    ):
        """ Добавляет новый рецепт в json """
        new_recipe = {
            "автор": author,
            "тип рецепта": recipe_type,
            "кухня": cuisine,
            "ингредиенты": ingredients,
            "описание": description,
            "url": url
        }
        self._recipes_json[recipe_name] = new_recipe
        self._save_file()



import json


class ConfigManager:

    def __init__(self, config_path: str):
        self._config_path = config_path
        try:
            self._config = self._load_config()
        except Exception as e:
            print(f"error: {str(e)}")
            raise

    def _load_config(self) -> dict:
        """ Загружаем данные из конфига """
        with open(self._config_path, "r", encoding="UTF-8") as file:
            data = json.load(file)
        return data

    def _save_config(self) -> None:
        """ Сохраняем данные в конфиг """
        with open(self._config_path, "w", encoding="UTF-8") as file:
            json.dump(self._config, file, ensure_ascii=False, indent=2)

    def get_data(self) -> dict:
        """ Возвращает все данные """
        return self._config

    def add_pizza(self, name: str, price: int, compounds: list) -> None:
        """ Добавить пиццу в конфиг """
        new_position = {
            "цена": price,
            "состав": compounds
        }
        self._config["pizza"][name] = new_position
        self._save_config()

    def add_topping(self, name: str, price: int) -> None:
        """ Добавить топпинг в конфиг """
        self._config["toppings"][name] = price
        self._save_config()

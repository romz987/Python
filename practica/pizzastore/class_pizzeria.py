import json
import logging
from abstracts import PizzeriaBase

# Настройка логирования
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # Устанавливаем уровень логирования

# Создаем обработчик для записи логов в файл
file_handler = logging.FileHandler('pizzeria.log')
file_handler.setLevel(logging.DEBUG)  # Уровень логирования для файла

# Создаем обработчик для вывода логов на консоль
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)  # Уровень логирования для консоли

# Создаем форматтер и добавляем его к обработчикам
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Добавляем обработчики к логгеру
logger.addHandler(file_handler)
logger.addHandler(console_handler)

class Pizzeria:

    def __init__(self, config_path: str):
        self._config_data = self._load_config(config_path)

    def _load_config(self, config_path: str):
        """ Загрузить конфиг """
        try:
            with open(config_path, "r") as file:
                data = json.load(file)
        except Exception as e:
            pass
            raise
        else:
            return data

    def _save_config(self) -> None:
        """ Сохранить конфиг """
        pass

    @abstractmethod 
    def get_menu(self) -> dict:
        """ Возвращает меню """
        pass

    @abstractmethod 
    def get_recipe(self, name: str) -> dict:
        """ Возвращает данные по конкретной пицце """
        pass

    @abstractmethod 
    def get_topping(self, name: str) -> dict:
        """ Возвращает данные по конкретному топпингу """
        pass

    @abstractmethod 
    def add_recipe(self, price: int, ingredients: list) -> None:
        """ Добавить рецепт пиццы """
        pass

    @abstractmethod 
    def add_topping(self, price: int, name: str) -> None:
        """ Добавить топпинг """
        pass

from abc import ABC, abstractmethod


class PizzeriaBase(ABC):

    @abstractmethod 
    def __init__(self, config_path: str):
        pass

    @abstractmethod
    def _load_config(self, config_path: str):
        """ Загрузить конфиг """
        pass

    @abstractmethod 
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


class KitchenBase(ABC):

    @abstractmethod 
    def __init__(self, recipe: list, topping: str):
        pass

    @abstractmethod 
    def prepare_base(self):
        """ Подготовить тесто """
        pass

    @abstractmethod 
    def prepare_sause(self):
        """ Подготовить соус """
        pass

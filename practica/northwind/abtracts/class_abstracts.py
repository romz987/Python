from abc import ABC, abstractmethod


class ConfigManagerBase(ABC):

    @abstractmethod
    def __init__(self, config_path: str):
        """ 
        Конструктор класса

        :param config_path: путь к конфигу 
        """
        pass

    @abstractmethod 
    def _load_config(self, config_path: str):
        """
        Загрузка информации из конфига
        """
        pass

    @abstractmethod 
    def get_tables(self):
        """
        Получение данных таблицы
        """
        pass


class DBCreatorAbstract(ABC):

    @abstractmethod
    def create_db(self, db_name: str) -> None:
        """ 
        Создание базы данных

        :param db_name: имя базы данных
        :return: None
        """
        pass
        
    @abstractmethod
    def create_table(self, table_data: dict) -> None:
        """
        Создание таблицы

        :param table_data: данные о таблице из json
        :return: None
        """
        pass


from abc import ABC, abstractmethod


class HomeworkBase:


    @abstractmethod 
    def __init__(self):
        pass


    @abstractmethod 
    def show_attr(self) -> str:
        """ Отобразить атрибут """
        pass


    @abstractmethod 
    def change_attr(self) -> None:
        """ Изменить атрибут """
        pass


    @abstractmethod 
    def pickle_data(self) -> None:
        """ Упаковать данные с помощью pikle"""
        pass


    @abstractmethod 
    def unpickle_data(self) -> None:
        """ Восстановить pickled данные """
        pass


    @abstractmethod 
    def save_data_to_json(self) -> None:
        """ Сохранить данные в json """
        pass


    @abstractmethod 
    def load_data_from_json(self) -> None:
        """ Восстановить данные из json """
        pass

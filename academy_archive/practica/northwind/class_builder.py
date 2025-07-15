from class_manager_csv import CsvManager
from class_repository import Repository

class RepositoryBuilder:


    @staticmethod 
    def build_repository(config_path: str) -> Repository:
        """ Строитель репозитория """
        csvman = CsvManager()
        return Repository(csvman) 

import json


class ShoesModel:


    def __init__(self, data_json_path: str):
        try: 
            self._shoes_assortment = self._load_file(data_json_path)
        except Exception:
            raise

    def _load_file(self, file_path: str):
        """ Загрузка файла """
        with open(file_path, "r", encoding="UTF-8") as file:
            data = json.load(file)
        return data

    def get_assortment(self):
        """ Получить весь доступный ассортимент """
        return self._shoes_assortment

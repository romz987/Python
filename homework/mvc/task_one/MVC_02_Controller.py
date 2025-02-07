from MVC_01_Model import ShoesModel


class ShoesController:


    def __init__(self, model: ShoesModel):
        self._model = model

    def get_assortment_all(self) -> dict:
        """ Получить весь ассортимент обуви """
        data = self._model.get_assortment()
        return data

    def get_assortment_man(self) -> dict:
        """ получить ассортимент обуви для мужчин """
        all_assortment = self.get_assortment_all()
        return all_assortment["man"]

    def get_assortment_woman(self) -> dict:
        """ получить ассортимент обуви для женщин """
        all_assortment = self.get_assortment_all()
        return all_assortment["woman"]

    def get_assortment_man_by_size(self, searched_size: int) -> list:
        """ 
        получить ассортимент обуви для мужчин 
        по размеру
        """
        answer = []
        all_assortment = self.get_assortment_man()
        for model, value in all_assortment.items():
            for size, data in value.items():
                if int(size) == searched_size:
                    result = {}
                    result[model] = data
                    answer.append(result)
        return answer

    def get_assortment_woman_by_size(self, searched_size: int) -> list:
        """ 
        получить ассортимент обуви для женщин 
        по размеру
        """
        answer = []
        all_assortment = self.get_assortment_woman()
        for model, value in all_assortment.items():
            for size, data in value.items():
                if int(size) == searched_size:
                    result = {}
                    result[model] = data
                    answer.append(result)
        return answer

    def get_assortment_man_by_color(self, color_name: str) -> list:
        """ 
        получить ассортимент обуви для мужчин 
        по цвету
        """
        answer = []
        all_assortment = self.get_assortment_man()
        for model, value in all_assortment.items():
            for size, data in value.items():
                result = {}
                price = data.get(color_name)
                if price:
                    result["model"] = model
                    result["size"] = size
                    result["color"] = color_name
                    result["price"] = price
                    answer.append(result)
        return answer

    def get_assortment_woman_by_color(self, color_name: str) -> list:
        """ 
        получить ассортимент обуви для женщин 
        по цвету
        """
        answer = []
        all_assortment = self.get_assortment_woman()
        for model, value in all_assortment.items():
            for size, data in value.items():
                result = {}
                price = data.get(color_name)
                if price:
                    result["model"] = model
                    result["size"] = size
                    result["color"] = color_name
                    result["price"] = price
                    answer.append(result)
        return answer



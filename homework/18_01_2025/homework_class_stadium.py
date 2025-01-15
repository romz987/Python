import json
import pickle
from abstract import HomeworkBase


class StadiumAdapter:
    def __init__(self, stadium):
        self.stadium = stadium

    def to_dict(self):
        """ Преобразовать атрибуты Stadium в словарь """
        return {
            "adress": self.stadium._Stadium__adress,
            "capacity": self.stadium._Stadium__capacity,
            "stadium_type": self.stadium._Stadium__stadium_type
        }


class Stadium(HomeworkBase):


    def __init__(self, adress: str, capacity: str, stadium_type: str):
        self.__adress = adress 
        self.__capacity = capacity 
        self.__stadium_type = stadium_type


    def show_attr(self, attr_name: str) -> str:
        """ 
        Отобразить атрибут 

        :param attr_name: имя атрибута
        :return: None
        """
        try:
            match attr_name:
                case "adress":
                    return self.__adress
                case "capacity":
                    return self.__capacity
                case "stadium_type":
                    return self.__stadium_type
                case _:
                    raise ValueError(f"{attr_name} attr not exists")
        except ValueError as ve:
            print({"error": str(ve)})
        except Exception as e:
            print({"error": str(e)})


    def change_attr(self, attr_name: str, new_value: str) -> None:
        """ 
        Изменить атрибут 

        :param attr_name: имя атрибута 
        :param new_value: новое значение
        :return: None
        """
        try: 
            match attr_name:
                case "adress":
                    self.__adress = new_value 
                case "capacity":
                    self.__capacity = new_value
                case "stadium_type":
                    self.__stadium_type = new_value
                case _:
                    raise ValueError(f"{attr_name} attr not exists")
        except ValueError as ve:
            print({"error": str(ve)})
        except Exception as e:
            print({"error": str(e)})


    def pickle_data(self, file_path: str) -> None:
        """ 
        Упаковать данные с помощью pikle

        :param file_path: имя файла для упаковки
        :return: None
        """
        try:
            attrs_dict = {
                "adress": self.__adress,
                "capacity": self.__capacity,
                "stadium_type": self.__stadium_type
            }
        except Exception as e:
            print({"error": str(e)})
        else:
            with open(file_path, "wb") as file:
                pickle.dump(attrs_dict, file)
            print("data pickled!")
     

    def unpickle_data(self, file_path: str) -> None:
        """ 
        Восстановить pickled данные 
        
        :param file_path: имя файла
        :return: None
        """
        try: 
            with open(file_path, "rb") as file:
                attr_dict = pickle.load(file)
                self.__adress = attr_dict["adress"]
                self.__capacity = attr_dict["capacity"]
                self.__stadium_type = attr_dict["stadium_type"]
        except Exception as e:
            print({"error": str(e)})
        else:
            print("data unpickled!")


    def save_data_to_json(self, file_name) -> None:
        """ 
        Сохранить данные как json 

        :param file_name: имя файла
        :return: None
        """
        try:
            adapter = StadiumAdapter(self)
            attrs_dict = adapter.to_dict()
            with open(file_name, "w") as file:
                json.dump(attrs_dict, file)
        except Exception as e:
            print({"error": str(e)})
        else:
            print("data jsoned!")


    def load_data_from_json(self, file_name) -> None:
        """ 
        Сохранить данные как json 

        :param file_name: имя файла
        :return: None
        """
        try:
            with open(file_name, "r") as file:
                attr_dict = json.load(file)
                self.__adress = attr_dict["adress"]
                self.__capacity = attr_dict["capacity"]
                self.__stadium_type = attr_dict["stadium_type"]
        except Exception as e:
            print({"error": str(e)})
        else:
            print("data loaded from json")




if __name__ == "__main__":
    auto = Stadium("Chkalova 5", "2500", "football")
    print(auto.show_attr("adress"))
    auto.show_attr("ololo")
    auto.change_attr("capacity", "370")
    print(auto.show_attr("capacity"))

    # Упаковка
    auto.pickle_data("pickled_auto.pkl")
    auto.change_attr("capacity", "3900")
    auto.save_data_to_json("stadium.json")
    # Распаковка
    auto.unpickle_data("pickled_auto.pkl")
    # Чек    
    print(auto.show_attr("capacity"))
    auto.load_data_from_json("stadium.json")
    print(auto.show_attr("capacity"))


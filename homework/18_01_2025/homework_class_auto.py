import json
import pickle
from abstract import HomeworkBase 


class Automobile(HomeworkBase):


    def __init__(self, model: str, color: str, age: str):
        self.__model = model 
        self.__color = color 
        self.__age = age


    def show_attr(self, attr_name: str) -> str:
        """ 
        Отобразить атрибут 

        :param attr_name: имя атрибута
        :return: None
        """
        try:
            match attr_name:
                case "model":
                    return self.__model
                case "color":
                    return self.__color
                case "age":
                    return self.__age
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
                case "model":
                    self.__model = new_value 
                case "color":
                    self.__color = new_value
                case "age":
                    self.__age = new_value
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
                "model": self.__model,
                "color": self.__color,
                "age": self.__age
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
                self.__model = attr_dict["model"]
                self.__color = attr_dict["color"]
                self.__age = attr_dict["age"]
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
            attrs_dict = {
                "model": self.__model,
                "color": self.__color,
                "age": self.__age
            }
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
                self.__model = attr_dict["model"]
                self.__color = attr_dict["color"]
                self.__age = attr_dict["age"]
        except Exception as e:
            print({"error": str(e)})
        else:
            print("data loaded from json")




if __name__ == "__main__":
    auto = Automobile("lada", "yellow", "15")
    print(auto.show_attr("model"))
    auto.show_attr("horse_power")
    auto.change_attr("color", "wheat")
    print(auto.show_attr("color"))

    # Упаковка
    auto.pickle_data("pickled_auto.pkl")
    auto.change_attr("color", "red")
    auto.save_data_to_json("auto.json")
    # Распаковка
    auto.unpickle_data("pickled_auto.pkl")
    # Чек    
    print(auto.show_attr("color"))
    auto.load_data_from_json("auto.json")
    print(auto.show_attr("color"))

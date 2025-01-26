import json
import pickle
from abstract import HomeworkBase 


class BookEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Book):
            return {
                "book_name": obj._Book__book_name,
                "author": obj._Book__author,
                "pages_count": obj._Book__pages_count,
                "date_of_realise": obj._Book__date_of_realise
            }
        return super().default(obj)


class Book(HomeworkBase):

    def __init__(self, book_name: str, author: str, pages_count: int, date_of_realise: str):
        self.__book_name = book_name 
        self.__author = author
        self.__pages_count = pages_count 
        self.__date_of_realise = date_of_realise


    def show_attr(self, attr_name: str) -> str:
        """ 
        Отобразить атрибут 

        :param attr_name: имя атрибута
        :return: None
        """
        try:
            match attr_name:
                case "book_name":
                    return self.__book_name
                case "author":
                    return self.__author
                case "pages_count":
                    return self.__pages_count
                case "date_of_realise":
                    return self.__date_of_realise
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
                case "book_name":
                    self.__name = new_value
                case "author":
                    self.__author = new_value
                case "pages_count":
                    self.__pages_count = new_value
                case "date_of_realise":
                    self.__date_of_realise= new_value
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
                "book_name": self.__book_name,
                "author": self.__author,
                "pages_count": self.__pages_count,
                "date_of_realise": self.__date_of_realise
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
                self.__book_name = attr_dict["book_name"]
                self.__author = attr_dict["author"]
                self.__pages_count = attr_dict["pages_count"]
                self.__date_of_realise= attr_dict["date_of_realise"]
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
            with open(file_name, "w") as file:
                json.dump(self, file, cls=BookEncoder)
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
                self.__book_name = attr_dict["book_name"]
                self.__author = attr_dict["author"]
                self.__pages_count = attr_dict["pages_count"]
                self.__date_of_realise= attr_dict["date_of_realise"]
        except Exception as e:
            print({"error": str(e)})
        else:
            print("data loaded from json")




if __name__ == "__main__":
    auto = Book("Mark Twain", "Adventures of Huckleberry Finn", "765", "1884")
    print(auto.show_attr("book_name"))
    auto.show_attr("publisher")
    auto.change_attr("pages_count", "355")
    print(auto.show_attr("pages_count"))

    # Упаковка
    print("Упакуем данные с помощью pickle, затем сменим количество страниц на 900 и сохраним как JSON\n")
    auto.pickle_data("pickled_auto.pkl")
    auto.change_attr("pages_count", "900")
    auto.save_data_to_json("book.json")
    print()
    # Распаковка
    print("Распакуем pickled data")
    auto.unpickle_data("pickled_auto.pkl")
    # Чек    
    print(auto.show_attr("pages_count"))
    auto.load_data_from_json("book.json")
    print(auto.show_attr("pages_count"))
    print(auto.show_attr("pages_count"))



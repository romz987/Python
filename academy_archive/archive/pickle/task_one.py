import pickle


class CountresData:


    def __init__(self):
        self.countres_dictionary = {}


    def add_value(self, country_name: str, capital_name: str) -> None:
        """ Добавить значение """
        self.countres_dictionary[country_name] = capital_name


    def delete_data(self, country_name: str) -> str:
        """ Удалить значение """
        for key, value in self.countres_dictionary.items():
            if key == country_name:
                deleted_value = self.countres_dictionary.pop(key)
                return deleted_value
        return "not found"


class CountresDatas:


    def __init__(self):
        self.countres_dictionary = {}


    def add_value(self, country_name: str, capital_name: str) -> None:
        """ Добавить значение """
        self.countres_dictionary[country_name] = capital_name


    def delete_data(self, country_name: str) -> str:
        """ Удалить значение """
        for key, value in self.countres_dictionary.items():
            if key == country_name:
                deleted_value = self.countres_dictionary.pop(key)
                return deleted_value
        return "not found"


class Pickler:


    def __init__(self, protocol: int = pickle.DEFAULT_PROTOCOL):
        self.protocol = protocol
        

    def pickle_file(self, data: CountresData, file_path):
        with open(file_path, "wb") as file:
            pickle.dump(data, file)



if __name__ == "__main__":
    countd = CountresDatas()
    countd.add_value('Belarus', 'Minsk')
    countd.add_value('Russia', 'Moscow')    
    countd.add_value('Kazakhstan', 'Astana')
    my_pkl = Pickler()
    my_pkl.pickle_file(countd, 'pickle_file')

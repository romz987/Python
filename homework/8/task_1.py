import pickle


class WorldCapitals:


    world_capitals_dict = {
        "Hunragy": "Budapest",
        "Serbia": "Belgrade",
        "France": "Paris",
        "Spain": "Madrid",
        "Italy": "Rome"
    }


    def __init__(self):
        pass 


    def add_data(self, contry_name: str, capital_name: str) -> str:
        self.world_capitals_dict[contry_name] = capital_name
        return (f"'{contry_name}: {capital_name}' added")


    def search_data(self, name: str) -> str:
        for key, value in self.world_capitals_dict.items():
            if key == name:
                return value
            if value == name:
                return key 
        return "searched data is not exists"
    

    def remove_data(self, name: str) -> str:
        for key, value in self.world_capitals_dict.items():
            if key == name or value == name:
                self.world_capitals_dict.pop(key)
                return (f"pair '{key}: {value}' deleted")


    def edit_data(self, data: str, new_data: str) -> str:
        for key, value in self.world_capitals_dict.items():
            if key == data:
                self.world_capitals_dict[new_data] = self.world_capitals_dict.pop(key)
                return f"key changed from {key} to {new_data}"
            if value == data:
                self.world_capitals_dict[key] = new_data
                return f"value changed from {value} to {new_data}"
        return "searched data is not exists"


    def pickle_data(self):
        try:
            with open("pickled_data_contries.pkl", "wb") as file:
                pickle.dump(self.world_capitals_dict, file)
        except Exception as e:
            print(f"error: {str(e)}")
        else:
            return "data pickled"


    def load_data(self):
        try:
            with open("pickled_data_contries.pkl", "rb") as file:
                data = pickle.load(file)
                self.world_capitals_dict = data
        except Exception as e:
            print(f"error: {str(e)}")
        else:
            return "data loaded"



if __name__ == "__main__":
    wcap = WorldCapitals() 

    print(wcap.add_data("Germany", "Berlin"))

    print(wcap.search_data("Spain"))

    print(wcap.remove_data("Serbia"))

    print(wcap.edit_data("Spain", "Strana"))

    print(wcap.edit_data("Paris", "Gorod"))

    print(wcap.world_capitals_dict)

    wcap.pickle_data()

    wcap.load_data()

    print(wcap.world_capitals_dict)


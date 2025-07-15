import pickle


class Airplane:


    def __init__(self, model: str, seats: int, _range: str):
        self.__model = model
        self.__seats = seats
        self.__range = _range


    def print_airplane_props(self):
        print(
            f"airplane model: {self.__model} has {self.__seats} available " 
            f"seats and has {self.__range} km max distance flight"
        )


def pickle_object(obj, filename):
    with open(filename, 'wb') as file:
        pickle.dump(obj, file)


def unpikle_object(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)



if __name__ == "__main__":
    air = Airplane("superjet", 250, 6000)
    air.print_airplane_props()


    pickle_object(air, "pickle_file.pkl")

    air2 = unpikle_object("pickle_file.pkl")

    air2.print_airplane_props()

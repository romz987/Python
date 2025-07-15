class Client:


    def __init__(self, name: str):
        self._name = name
        self._books = []

    def get_name(self):
        """ Вернуть имя клиента """
        return self._name

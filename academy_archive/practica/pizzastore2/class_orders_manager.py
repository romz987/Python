class OrdersManager:

    def __init__(self, file_path: str):
        self.__file_path = file_path

    def save_order(self, order) -> None:
        """ 
        Сохранить заказ 

        :param order: объект пиццы
        """
        with open(self.__file_path, "a", encoding="utf-8") as file:
            file.write(str(order))    

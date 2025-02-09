class Order:

    def __init__(
        self,
        name: str,
        toppings: list,
        price: str
    ):
        self._name = name 
        self._toppings = toppings 
        self._total_price = price

    def get_total_price(self) -> int:
        """ Возвращает стоимость заказа """
        return self._total_price

    def __str__(self) -> None:
        """ Информация о заказе """
        return f"Пицца: {self._name}\nТоппинги: {self._toppings}\nЦена: {self._total_price}\n\n"

from class_pizzeria_model import PizzeriaModel 
from class_pizzeria_order import Order

class PizzeriaController:


    def __init__(self, model: PizzeriaModel, order: type):
        self._model = model
        self._Order = order
        self._orders = []


    def get_full_menu(self) -> dict:
        """ Получить из модели все данные меню """
        return self._model.get_menu()

    def get_pizza_menu(self) -> dict:
        """ Получить меню пиццы """
        data = self.get_full_menu()
        return data["pizza"]

    def get_toppings_menu(self) -> dict:
        """ Получить меню пиццы """
        data = self.get_full_menu()
        return data["toppings"]

    def order_pizza(self, pizza_name: str, toppings: list):
        """ Заказать пиццу """
        pizza_menu = self.get_pizza_menu()
        topping_menu = self.get_toppings_menu()
        try:
            pizza_data = pizza_menu[pizza_name]
            total_price = int(pizza_data["цена"])
            # топпинги
            if len(toppings) > 0:
                for topping in toppings:
                    total_price += int(topping_menu[topping])

        except KeyError:
            print("В меню нет такой позиции")
        except Exception as e:
            print(f"error: {str(e)}")
        else:
            order = Order(pizza_name, toppings, total_price)
            self._orders.append(order)
            self.save_order_to_file(order)
            return order

    def save_order_to_file(self, order: Order):
        """ Сохранить заказ в файл """
        self._model.save_order(order)   

    def get_orders_summary(self):
        """ Отчет по заказам """
        if len(self._orders) > 0:
            total_profit = 0
            for order in self._orders:
                total_profit += int(order.get_total_price())
            result = {
                'total_count': len(self._orders),
                'total_profit': total_profit,
            }
            return result
        return False


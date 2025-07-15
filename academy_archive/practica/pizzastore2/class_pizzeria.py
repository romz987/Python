from class_config_manager import ConfigManager
from class_orders_manager import OrdersManager
from class_pizza import Pizza


class Pizzeria:

    def __init__(
        self, 
        config_manager: ConfigManager,
        orders_manager: OrdersManager,
        class_pizza: type[Pizza]
    ):
        self.__orders = []
        self.__config_manager = config_manager
        self.__orders_manager = orders_manager
        self.__class_pizza = class_pizza

    def method(self):
        pass

    def get_menu_pizza(self) -> dict:
        """ Показать ассортимент пиццы """
        data = self.__config_manager.get_data()
        return data["pizza"]

    def get_menu_toppings(self) -> dict:
        """ Показать ассортимент пиццы """
        data = self.__config_manager.get_data()
        return data["toppings"]

    def add_order(self, pizza_name: str, toppings_list: list) -> str:
        """ 
        Сделать заказ 

        :param pizza_name: название пиццы
        :param toppings_list: список топпингов[опционально]
        :return: строка состояния
        """
        try:
            # Получаем доступные позиции
            pizza_menu = self.get_menu_pizza()
            toppings_menu = self.get_menu_toppings()
            # Получаем информацию о пицце 
            pizza_data = pizza_menu[pizza_name]
            total_price = int(pizza_data["цена"])
            # Топпинги
            if len(toppings_list) > 0:
                for topping in toppings_list:
                    total_price += int(toppings_menu[topping])
        except KeyError:
            print("В меню нет такой позиции")
        except Exception as e:
            print(f"error: {str(e)}")
        else:
            order = self.__class_pizza(pizza_name, toppings_list, total_price)
            self.__orders.append(order)
            self.__orders_manager.save_order(order)
            return "ok"

    def get_orders_summary(self) -> dict:
        """ Отчет по заказам """
        if len(self.__orders) > 0:
            total_profit = 0
            for order in self.__orders:
                total_profit += int(order.get_total_price())
            result = {
                'total_count': len(self.__orders),
                'total_profit': total_profit,
            }
            return result
        return False

    def add_new_pizza_to_menu(self, name: str, price: int, compounds: str) -> None:
        """ 
        Добавить новую пиццу в меню 

        :param name: название пиццы 
        :param price: цена пиццы
        :param compounds: состав пиццы
        """
        self.__config_manager.add_pizza(name, price, compounds)

    def add_new_topping_to_menu(self, name: str, price: int) -> None:
        """ 
        Добавить новый топпинг в меню

        :param name: название пиццы 
        :param price: цена пиццы
        """
        self.__config_manager.add_topping(name, price)

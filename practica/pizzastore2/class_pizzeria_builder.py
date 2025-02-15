from class_config_manager import ConfigManager
from class_orders_manager import OrdersManager
from class_pizzeria import Pizzeria
from class_pizza import Pizza


class PizzeriaBuilder:

    @staticmethod
    def build_pizzeria(
        config_path: str,
        orders_file_path: str,
        class_config_manager: type[ConfigManager],
        class_orders_manager: type[OrdersManager],
        class_pizzeria: type[Pizzeria], 
        class_pizza: type[Pizza]
    ):
        """ 
        Построить пиццерию 

        :param class_config_manager: класс менеджер конфигурации
        :param class_orders_manager: класс менеджер заказов
        :param class_pizzeria: класс пиццерии 
        :param class_pizza: класс пицца
        :return: экземпляр класса пиццерии
        """
        config_manager = class_config_manager(config_path)
        orders_manager = class_orders_manager(orders_file_path)
        return class_pizzeria(config_manager, orders_manager, class_pizza)

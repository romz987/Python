from class_pizzeria_controller import PizzeriaController 


class PizzeriaView:

    def __init__(self, controller: PizzeriaController):
        self._controller = controller 

    def show_pizza_menu(self) -> None:
        """ Показать меню пиццы """
        menu = self._controller.get_pizza_menu()
        for pizza_nama, pizza_info in menu.items():
            print(f"Пицца: {pizza_nama}")
            print(f"Состав: {pizza_info["состав"]}")
            print(f"Цена: {pizza_info["цена"]} руб.")
            print()

    def show_toppings_menu(self) -> None:
        """ Показать меню топпингов """
        menu = self._controller.get_toppings_menu()
        for topping_name, topping_price in menu.items():
            print(f"Топпинг: {topping_name}")
            print(f"Цена: {topping_price}")
            print()

    def show_orders_summary(self) -> None:
        """ Показать отчет по заказам """
        summary = self._controller.get_orders_summary()
        if summary:
            print(f"Количество заказанных пицц: {summary["total_count"]}")
            print(f"Общая сумма заказов: {summary["total_profit"]}")
            print()
        else:
            print("На данный момент заказов нет")
            print()

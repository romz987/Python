def show_menu_pizza(menu_pizza: dict) -> None:
    """ Выводит ассортимент пиццы на экран """
    for pizza_nama, pizza_info in menu_pizza.items():
        print(f"Пицца: {pizza_nama}")
        print(f"Состав: {pizza_info["состав"]}")
        print(f"Цена: {pizza_info["цена"]} руб.")
        print()

def show_menu_toppings(menu_toppings: dict) -> None:
    """ Выводит ассортимент топпингов на экран """
    for topping_name, topping_price in menu_toppings.items():
        print(f"Топпинг: {topping_name}")
        print(f"Цена: {topping_price}")
        print()

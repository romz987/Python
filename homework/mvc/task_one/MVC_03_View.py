from MVC_02_Controller import ShoesController 


class ShoesView: 


    def __init__(self, controller: ShoesController):
        self._controller = controller

    def show_all_assortment(self) -> None:
        """ Показать весь ассортимент """
        data = self._controller.get_assortment_all()
        # Выводим женский ассортимент
        print("Ассортимент женской обуви: ")
        print()
        woman_assortment = data["woman"]
        for model, value in woman_assortment.items():
            for size, showes_data in value.items():
                for color, price in showes_data.items():
                    print(f"Марка: {model}")
                    print(f"Размер: {size}")
                    print(f"Цвет: {color}")
                    print(f"Цена: {price} руб.")
                    print()

        print("Ассортимент мужской обуви: ")
        print()
        man_assortment = data["man"]
        for model, value in man_assortment.items():
            for size, showes_data in value.items():
                for color, price in showes_data.items():
                    print(f"Марка: {model}")
                    print(f"Размер: {size}")
                    print(f"Цвет: {color}")
                    print(f"Цена: {price} руб.")
                    print()

    def show_woman_assortment(self) -> None:
        """ Показать ассортимент женской обуви """
        data = self._controller.get_assortment_all()
        # Выводим женский ассортимент
        print("Ассортимент женской обуви: ")
        print()
        woman_assortment = data["woman"]
        for model, value in woman_assortment.items():
            for size, showes_data in value.items():
                for color, price in showes_data.items():
                    print(f"Марка: {model}")
                    print(f"Размер: {size}")
                    print(f"Цвет: {color}")
                    print(f"Цена: {price} руб.")
                    print()

    def show_man_assortment(self) -> None:
        """ Показать ассортимент мужской обуви """
        data = self._controller.get_assortment_all()
        print("Ассортимент мужской обуви: ")
        print()
        man_assortment = data["man"]
        for model, value in man_assortment.items():
            for size, showes_data in value.items():
                for color, price in showes_data.items():
                    print(f"Марка: {model}")
                    print(f"Размер: {size}")
                    print(f"Цвет: {color}")
                    print(f"Цена: {price} руб.")
                    print()

    def show_woman_assortment_by_size(self, size: int) -> None:
        """ Показать женский ассортмент по раземру """
        data = self._controller.get_assortment_woman_by_size(size)
        print(f"Женская обувь, размер {size}:")
        print()
        for i in data:
            for model, showes_data in i.items():
                for color, price in showes_data.items():
                    print(f"Марка: {model}")
                    print(f"Цвет: {color}")
                    print(f"Цена: {price}")
                    print()

    def show_man_assortment_by_size(self, size: int) -> None:
        """ Показать мужской ассортмент по раземру """
        data = self._controller.get_assortment_man_by_size(size)
        print(f"Мужская обувь, размер {size}:")
        print()
        for i in data:
            for model, showes_data in i.items():
                for color, price in showes_data.items():
                    print(f"Марка: {model}")
                    print(f"Цвет: {color}")
                    print(f"Цена: {price}")
                    print()

    def show_woman_assortment_by_size(self, color: str) -> None:
        """ Показать женский ассортмент по раземру """
        data = self._controller.get_assortment_woman_by_color(color)
        print(data)

    def show_man_assortment_by_size(self, color: str) -> None:
        """ Показать мужской ассортмент по раземру """
        data = self._controller.get_assortment_man_by_color(color)
        print(data)

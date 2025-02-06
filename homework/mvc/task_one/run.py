from MVC_01_Model import ShoesModel
from MVC_02_Controller import ShoesController
from MVC_03_View import ShoesView


if __name__ == "__main__":
    model = ShoesModel("data.json")
    controller = ShoesController(model)
    view = ShoesView(controller) 
    # print(controller.get_assortment_all())
    # print()
    # print(controller.get_assortment_man())
    # print()
    # print(controller.get_assortment_man_by_size(41))
    # print(controller.get_assortment_woman_by_size(39))
    # print(controller.get_assortment_man_by_color("red"))
    # print(controller.get_assortment_woman_by_color("brown"))

    # Весь ассортимент
    # print(view.show_man_assortment())

    print(view.show_man_assortment_by_size(40))

    print("buy")

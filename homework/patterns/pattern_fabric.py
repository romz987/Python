from abc import ABC, abstractmethod 


class PastaBuilderBase(ABC):


    @abstractmethod 
    def pasta_type(self) -> str:
        """ Тип пасты """
        pass


    @abstractmethod 
    def sauce(self) -> str:
        """ Добавляемый соус """
        pass


    @abstractmethod 
    def filling(self) -> str:
        """ Используемая начинка """
        pass


    @abstractmethod 
    def additives(self) -> str:
        """ Дополнительные добавки """
        pass


    @abstractmethod 
    def __str__(self) -> str:
        """ Информация об объекте """
        pass


class FabricaPastaBase(ABC):
    """ Абстрактная фабрика """

    @abstractmethod 
    def __init__(self):
        pass 


    @abstractmethod 
    def get_pasta_maker(self):
        pass


class PastaBuilder(PastaBuilderBase):
    """ Сборщик блюда """

    def __init__(
            self, 
            pasta_name: str,
            pasta_type: str, 
            sauce: str, 
            filling: str, 
            additives: str):
        self.__pasta_name = pasta_name
        self.__pasta_type = pasta_type
        self.__sauce = sauce 
        self.__filling = filling 
        self.__additives = additives


    def pasta_type(self) -> str:
        """ Тип пасты """
        return self.__pasta_type 


    def sauce(self) -> str:
        """ Добавляемый соус """
        return self.__sauce


    def filling(self) -> str:
        """ Используемая начинка """
        return self.__filling


    def additives(self) -> str:
        """ Начинка """
        return self.__additives


    def __str__(self) -> str:
        """ Информация об объекте """
        return (
            f"Наша паста это:\n"
            f"{self.__pasta_name.upper()}\n"
            f"{self.pasta_type()}\n"
            f"{self.sauce()}\n"
            f"{self.filling()}\n"
            f"{self.additives()}"
        )


class PastaRecipes:

    pasta_with_cutlets = [
        "Макароны с котлетами",
        "Макароны фузинни",
        "Томатный кетчуп с чесноком",
        "Две котлеты",
        "Прованские травы"
    ]
        
    pasta_carbonara = [
        "Паста карбонара",
        "Спагетти",
        "Сливочный соус",
        "Грибы",
        "Французские травы"
    ] 

    pasta_bolognese = [
        "Паста бологнесе",
        "Спагетти",
        "Томатная паста",
        "Фарш",
        "Орегано"
    ]

    def get_pwcutlets_recipe(self) -> list:
        """ Получить рецент пасты """
        return self.pasta_with_cutlets


    def get_pasta_carbonara(self) -> list:
        """ Получить рецент пасты """
        return self.pasta_carbonara


    def get_pasta_bolognese(self) -> list:
        """ Получить рецент пасты """
        return self.pasta_bolognese


class FabricaPasta(FabricaPastaBase):
    """ Фабрика пасты """

    def __init__(self, recipes: PastaRecipes):
        self.__recipes = recipes


    def get_pasta_maker(self, pasta_name: str):
        match pasta_name:
            case "pasta_with_cutlets":
                recipe = self.__recipes.get_pwcutlets_recipe()
                pbuilder = PastaBuilder(
                    recipe[0], 
                    recipe[1], 
                    recipe[2], 
                    recipe[3], 
                    recipe[4]
                )
                return pbuilder

            case "pasta_carbonara":
                recipe = self.__recipes.get_pasta_carbonara()
                pbuilder = PastaBuilder(
                    recipe[0], 
                    recipe[1], 
                    recipe[2], 
                    recipe[3], 
                    recipe[4]
                )
                return pbuilder

            case "pasta_bolognese":
                recipe = self.__recipes.get_pasta_bolognese()
                pbuilder = PastaBuilder(
                    recipe[0], 
                    recipe[1], 
                    recipe[2], 
                    recipe[3], 
                    recipe[4]
                )
                return pbuilder

            case _:
                # Ну например так
                raise ValueError(
                    f"{pasta_name} - неправильное имя пасты"
                )



if __name__ == "__main__":

    pasta_recipes = PastaRecipes()
    fabrica = FabricaPasta(pasta_recipes)

    # Получаем сборщик пасты из фабрики
    try:
        pasta = fabrica.get_pasta_maker("pasta_carbonara")
    except Exception as e:
        print(f"error: {str(e)}")
    else:
        print(pasta.__str__())

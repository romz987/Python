class Refrig:
    """ Задание 8.1.2 холодильник """

    def __init__(self, model: str, age: int, volume: int):
        self.model = str(model)
        self.age = int(age)
        self.volume = int(volume)
        self.free_volume = int(self.volume)
        self.products = {}


    def get_model(self):
        return self.model

     
    def get_age(self):
        return self.age


    def get_volume(self):
        return self.volume


    def get_products(self):
        if len(self.products) == 0:
            print('В холодильнике пусто!')
            return
        print('У нас есть: ')
        for key, value in self.products.items():
            print(f'{key}, которые занимают {value} литров')


    def get_free_volume(self):
        return(self.free_volume)


    def add_prodcut(self):
        products_name = str(
            input('Какой продукт положим в холодильник?: ')
        )
        product_volume = int(
            input('Какой объем занимает продкут в литрах?: ')
        )
        if product_volume < self.free_volume:
            self.products[products_name] = product_volume
            self.free_volume = self.free_volume - product_volume
        else:
            print('Не хватает места!')


if __name__ == "__main__":
    
    ref_one = Refrig('ariston', 25, 150)
    ref_two = Refrig('lg', 2, 100)
    answer = 1

    # Для работы с объектом ref_two все ref_one надо заменить на ref_two
    while answer != 0:
        print('Введите 1 чтобы увидеть модель холодильника')
        print('Введите 2 чтобы увидеть возраст холодильника')
        print('Введите 3 чтобы увидеть объем холодильника')
        print('Введите 4 чтобы увидеть что уже есть в холодильнике')
        print('Введите 5 чтобы добавить продукт в холодильник')
        print('Введите 6 чтобы увидить свободный объем')
        print('Введите 0 чтобы выйти')
        answer = int(input('Ваш выбор: '))

        if answer == 1:
            print(ref_one.get_model())
        elif answer == 2:
            print(ref_one.get_age())
        elif answer == 3:
            print(ref_one.get_volume())
        elif answer == 4:
            ref_one.get_products()
        elif answer == 5:
            ref_one.add_prodcut() 
        elif answer == 6: 
            print(ref_one.get_free_volume())
        elif answer == 0:
            pass 
        else:
            print('Ответ должен содержать число от 0 до 6')



        



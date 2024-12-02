class Vehicle:


    def __init__(self, name: str, mileage: int):
        self.name = str(name)
        self.mileage = int(mileage)


    def get_vehicle_type(self, wheels_count: int):
        try:
            if wheels_count < 0 or wheels_count > 4:
                return 'Я не знаю таких ТС'
            elif wheels_count == 1:
                return f'Это моноколесо марки {self.name}'
            elif wheels_count == 2:
                return f'Это мотоцикл марки {self.name}'
            elif wheels_count == 3:
                return f'У Вашего {self.name} украли колесо!'
            elif wheels_count == 4:
                return f'Это автомобиль марки {self.name}'

        except Exception as e:
            print(f'Error! {str(e)}')


    def get_vehicle_advice(self):
        if self.mileage < 50000:
            print(f'Неплохо, {self.name} можно брать!')
        elif self.mileage < 100000:
            print(f'{self.name} - надо внимательно проверить!')
        elif self.mileage < 150000:
            print(f'{self.name} - надо провести полную диагностику')
        else:
            print(f'{self.name} - лучше не покупать')


if __name__ == "__main__":
    vh_one = Vehicle('vaz', 120000)
    vh_two = Vehicle('maz', 45000)
    vh_three = Vehicle('jugo', 800000)
    vh_four = Vehicle('lancia', 45000)

    print(vh_one.get_vehicle_type(1))
    print(vh_two.get_vehicle_type(2))
    print(vh_three.get_vehicle_type(3))
    print(vh_four.get_vehicle_type(4))
    print(vh_one.get_vehicle_type('hello'))

    vh_one.get_vehicle_advice()
    vh_two.get_vehicle_advice()
    vh_three.get_vehicle_advice()
    vh_four.get_vehicle_advice()

class AutoDoors:
    """ Двери автомобиля """
    valid_colors = [
        'красный',
        'синий',
        'желтый',
        'баклажан'
    ]

    def __init__(self):
        self._door_count = 0
        self._door_color = ''


    @property 
    def door_count(self):
        return self._door_count


    @property 
    def door_color(self):
        return self._door_color 


    @door_count.setter 
    def door_count(self, value):
        if not isinstance(value, int):
            raise ValueError('Недопустимое значение дверей')
        self._door_count = value


    @door_color.setter 
    def door_color(self, value):
        if value not in self.valid_colors:
            raise ValueError('Недопустимый цвет')
        self._door_color = value


class AutoWheels(AutoDoors):
    """ Колеса автомобиля """

    def __init__(self):
        super().__init__()
        self._wheels_count = 0


    @property 
    def wheels_count(self):
        return self._wheels_count 


    @wheels_count.setter 
    def wheels_count(self, value):
        if not isinstance(value, int):
            raise ValueError('Недопустимое значение колес')
        self._wheels_count = value



class AutoEngine(AutoWheels):
    """ Двигатель автомобиля """

    def __init__(self):
        super().__init__()
        self._engine_hp = 0


    @property  
    def engine_hp(self):
        return self._engine_hp 


    @engine_hp.setter  
    def engine_hp(self, value):
        if not isinstance(value, int):
            raise ValueError('Недопустимое значение мощности двигателя')
        self._wheels_count = value


class DasAuto(AutoEngine):
    """ Автомобиль """

    def __init__(self, name):
        super().__init__()
        self.name = name


    def conclusion(self):
        check_doors = self.door_count > 1 and self.door_count < 6
        check_wheels = self.wheels_count > 0 and self.wheels_count < 5
        check_engine_hp = self.engine_hp > 10 and self.engine_hp < 750

        if check_doors and check_wheels and check_engine_hp:
            print(f'Это нормальный автомобиль {self.name}')
        else:
            print(f'Это странный автомобиль {self.name}')

        if self.door_color != '':
            print(f'С дверями цвета: {self.door_color}')


if __name__ == "__main__":
    au = DasAuto('WV')

    au.door_count = 4
    au.door_color = 'баклажан'
    au.wheels_count = 7 
    au.engine_hp = 150 

    au.conclusion()

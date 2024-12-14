class Circle:


    def __init__(self):
        self._radius = 0


    @property
    def radius(self):
        return self._radius 


    @radius.setter 
    def radius(self, value):
        try:
            if value > 0:
                self._radius = value
            else:
                raise Exception(
                    'Значение может быть ' 
                    'только положительным числом'
                )
        except Exception as e:
            print({'error': str(e)})


class Square(Circle):


    def __init__(self):
        super().__init__()
        self._side_length = 0


    @property
    def side_length(self):
        return self._side_length


    @side_length.setter 
    def side_length(self, value):
        try:
            if value > 0:
                self._side_length = value
            else:
                raise Exception(
                    'Значение может быть ' 
                    'только положительным числом'
                )
        except Exception as e:
            print({'error': str(e)})


class CircleInSquare(Square):


    def __init__(self):
        super().__init__()


    def size(self):
        radius = self.radius
        side_length = self.side_length
        if radius != 0:
            side_length = radius * 2
            print(
                f'Если радиус окружности {radius}\n'
                f'То длинна стороны квадрата: {side_length}\n'
            )
        elif side_length != 0:
            radius = side_length / 2
            print( 
                f'Если длинна стороны квадрата {side_length}\n'
                f'То радиус окружности: {radius}\n'
            )
        else: 
            print('Размеры не заданы')



if __name__ == "__main__":
    cis = CircleInSquare()

    cis.side_length = 12

    cis.size()

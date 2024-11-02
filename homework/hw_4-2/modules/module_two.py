def module_two_hello():
    """
    Приветствие
    """
    print(
        'Привет! Я функция из второго модуля!\n'
    )


def numbers_diff(number_one: int, number_two: int) -> int:
    """
    Вычитает первое число из второго числа

    :param number_one: первое число
    :param number_two: второе число 
    :return: сумма двух чисел
    """
    try:
        if not isinstance(number_one, int) or not isinstance(number_two, int):
            raise TypeError('Ожидается целое число')
    except TypeError as e:
        print('Ошибка:', e)
    else: 
        result = number_two - number_one
        print(f'Результат: {result}')
        return result
    finally:
        print('Мы закончили')

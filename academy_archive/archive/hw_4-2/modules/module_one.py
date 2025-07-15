def module_one_hello():
    """
    Приветствие
    """
    print(
        'Привет! Я функция из первого модуля!\n'
    )


def numbers_sum(number_one: int, number_two: int) -> int:
    """
    Складывает два числа

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
        result = number_one + number_two
        print(f'Сумма чисел: {result}')
        return result
    finally:
        print('Мы закончили')





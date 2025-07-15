# Кортеж со строками 
genres_tuple = (
    'Роман',
    'Новелла',
    'Фэнтези',
    'Научная фантастика'
)
# Кортеж с целочисленными значениями
numbers_tuple = 3, 7, 9, 1, 6, 8, 2, 5, 4


def check_tuple_length(_tuple):
    """
    Выводит длину кортежа

    :param _tuple: любой кортеж
    :return: None
    """
    print(f'Длина кортежа: {len(_tuple)}')


def tuple_min_max(_tuple):
    """
    Выводит максимальный и минимальный элементы

    :param _tuple: любой кортеж
    :return: None
    """
    print(f'максимальный элемент: {max(_tuple)}')
    print(f'минимальный элемент: {min(_tuple)}')


def smartass_tuple_sum(_tuple):
    """
    Выводит сумму элементов кортежа
    Даже если это строки

    :param _tuple: любой кортеж
    :return: None
    """
    current_var_str = ''
    current_var_num = 0

    for i in _tuple:
        if isinstance(i, str):
            current_var_str += i
        else:
            current_var_num += i

    if isinstance(i, str):
        print(f'Сумма элементов кортежа: {current_var_str}')
    else:
        print(f'Сумма элементов кортежа: {current_var_num}')


def regular_tuple_sum(_tuple):
    """
    Выводит сумму элементов кортежа
    Только если в кортеже числовые значения

    :param _tuple: любой кортеж
    :return: None
    """
    try:
        result = sum(_tuple)
    except TypeError:
        print('Строки сложить не выйдет')
    else:
        print(f'Сумма элементов кортежа: {result}')
    

def sorted_tuple(_tuple) -> tuple:
    """
    Возвращает отсортированный кортеж

    :param _tuple: любой кортеж
    :return: None
    """
    result_tuple = sorted(_tuple)

    print(f'Сортированный кортеж: {result_tuple}')
    
    return result_tuple

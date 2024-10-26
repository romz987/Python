# Домашнее задание 

def bill_hates():
    """
    Выводит на экран цитату Билла Гейтса

    :return: None
    """
    author = "Bill Gates"

    print(
        '"Don\'t compare yourself with anyone in this world...\n'
        ' if you do so, you are insulting yourself.\"\n'
        f'{author.rjust(50)}'
    )


def even_numbers(num_one: int, num_two: int):
    """ 
    Выводит все четные числа в заданном пользователем
    диапазоне

    :num_one: нижняя граница диапазона 
    :num_two: верхняя граница диапазона
    :return: None 
    """
    for i in range(num_one, num_two + 1):
        if i % 2 == 0:
            print(i)


def art_square(length: int, empty: bool):
    """
    Выводит квадрат указанной длинны стороны 
    из указанного символа

    :length: длинна стороны
    :empty: True - пустой квадрат, False - заполненный квадрат
    :return: None
    """

    if empty:
        for i in range(0, length):
            if i == 0 or i == length - 1:
                print('#'.ljust(length * 3, "#"))
            else:
                print('#' + (length * 3 -2) * ' ' + '#')

    else:
        for _ in range(0, length):
            print('#'.ljust(length * 3, "#"))


def min_number(*args):
    """
    Если указано пять чисел в качестве аргументов 
    выводит минимальное из них

    :return: None
    """
    if len(args) != 5:
        print('Неверные аргументы')
    
    var = args[0]
    for i in args:
        if i < var:
            var = i 

    print(var)


def numbers_product(num_one: int, num_two: int):
    """ 
    Произведение чисел в переданном диапазоне с нормализацией
    
    :num_one: нижняя граница диапазона
    :num_two: верхняя граница диапазона
    :return: None
    """
    if num_one > num_two:
        num_one, num_two = num_two, num_one 

    result = 1
    for i in range(num_one, num_two + 1):
        if i != 0:
            result *= i

    print(result)

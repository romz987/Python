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



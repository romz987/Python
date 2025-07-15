import random
import queue
from queue import Queue

q = queue.Queue()

def list_random_gen(q: Queue, count: int) -> None:
    """ 
    Создает список, заполненный случайными числами 

    :param q: экземпляр класса потокобезопасная очередь
    :param count: количество элементов в списке
    """
    result = []
    for _ in range(count):
        result.append(random.randint(1, 1000))
    q.put(result)


def list_sum_numbers(q: Queue, _list: list) -> None:
    """
    Создает сумму элементов списка

    :param q: экземпляр класса потокобезопасная очередь
    :param _list: список натуральных чисел
    """
    q.put(sum(_list))


# Находит среднеарифмитическое элементов списка
def list_arithmetic_mean(q: Queue, _list: list) -> None:
    """ 
    Среднее арифметическое

    :param q: экземпляр класса потокобезопасная очередь
    :param _list: список натуральных чисел
    """
    q.put(sum(_list) / len(_list))

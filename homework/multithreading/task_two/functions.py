import random
import queue

q = queue.Queue()

# Создание файла со случайными числами
def gen_random_list(count: int) -> list:
    """ Создает список со случайными числами """
    result = []
    for _ in range(count):
        result.append(random.randint(0, 1000))
    return result

def save_file(file_path: str, _list: list) -> None:
    """ Сохраняет файл """
    with open(file_path, "w", encoding="utf-8") as file:
        for i in _list:
            file.write(str(i) + '\n')

def create_file_random_num(file_path: str, count: int):
    """ Создает файл со случайными числами """
    _list = gen_random_list(count)
    save_file(file_path, _list)


# Работа с созданным файлом:
def read_file(file_path: str) -> list:
    """ Открывает файл и сериализует данные из него в список """
    result = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            result.append(int(line.strip()))
    return result


# Проверка на простоту
def is_simple(_list: list):
    """ Находит все простые числа """
    _list = read_file(file_path)
    result = []
    for i in list



import random


# Создание файла со случайными числами
def gen_random_list(count: int) -> list:
    """ Создает список со случайными числами """
    result = []
    for _ in range(count):
        result.append(random.randint(1, 100))
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
def check_file_for_primes(file_path: str):
    """ Точка входа """
    file_list = read_file(file_path)
    result = is_prime(file_list)
    save_file("primes.txt", result)

def is_prime(_list: list) -> list:
    """ Находит все простые числа """
    result = []
    for num in _list:
        prime = True
        if num > 2:
            for j in range(2, round(num/2+1)):
                if num % j == 0:
                    prime = False
        if prime:
            result.append(num)
    return result

# Факториал
def calc_factorial_in_file(file_path: str):
    """ Точка входа """
    file_list = read_file(file_path)
    result = calculate_factorial(file_list)
    save_file("factorials.txt", result)

def calculate_factorial(_list: list) -> list:
    """ Считает факториал каждого числа """
    result = []
    for num in _list:
        a = 1
        for j in range(1, num + 1):
            a = a * j
        result.append(f"Факториал числа {num} : {a}")
    return result




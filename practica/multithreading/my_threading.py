import threading

def open_file(file_path: str) -> list:
    """ Открыть файл """
    with open(file_path, "r", encoding="UTF-8") as file:
        numbers = file.readlines()
        return numbers


def save_file(file_path: str, _list: list) -> None:
    """ Записать в файл """
    with open(file_path, "w", encoding="UTF-8") as file:
        for number in _list:
            file.write(f"{number}\n")


def get_even(numbers_list, file_name="even_numbers.txt"):
    """ Выбрать четные """
    result = []
    for i in numbers_list:
        number = int(i.strip())
        if number % 2 == 0:
            result.append(str(number))
    save_file(file_path=file_name, _list=result)
    return result


def get_odd(numbers_list, file_name="odd_numbers.txt"):
    """ Выбрать нечетные """
    result = []
    for i in numbers_list:
        number = int(i.strip())
        if number % 2 != 0:
            result.append(str(number))
    save_file(file_path=file_name, _list=result)
    return result






if __name__ == "__main__":
    file_path = input("Введите путь к файлу: ")
    numbers_list = open_file(file_path)
    # print(numbers_list)
    # print("Четные: ")
    # print(get_even(numbers_list))
    # print("Нечетные: ")
    # print(get_odd(numbers_list))

    thread1 = threading.Thread(target=get_odd, args=(numbers_list,))
    thread2 = threading.Thread(target=get_even, args=(numbers_list,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()



# Поправил паттерн для проверки почты
# Прошлый паттерн действительно не работал...


import re


def set_user_info() -> list:
    """
    Создает список с данными пользователя

    :return: None
    """

    name_pattern = r'^[a-zA-Zа-яА-ЯёЁ]+$'
    phone_pattern = r'^\+\d{1,3}\(\d{2}\)\d{7}$'
    email_pattern = r'^[a-zA-Z0-9]+@yandex\.ru$'

    user_data_list = []

    while True:
        user_name = input('Введите Ваше имя: ')
        check = bool(re.match(name_pattern, user_name))

        if check:
            print('Имя принято')
            user_data_list.append(user_name)
            break
        else:
            print('Вы ввели неверное имя пользователя! Попробуйте еще раз!')

    while True:
        user_surname = input('Введите Вашу фамилию: ')
        check = bool(re.match(name_pattern, user_surname))

        if check:
            print('Фамилия принята')
            user_data_list.append(user_surname)
            break
        else:
            print('Вы ввели неверную фамилию! Попробуйте еще раз!')

    while True:
        user_phone = input('Введите номер телефона: ')
        check = bool(re.match(phone_pattern, user_phone))

        if check:
            print('Номер телефона принят')
            user_data_list.append(user_phone)
            break
        else:
            print('Вы ввели неверный номер телефона! Попробуйте еще раз!')

    while True:
        user_email = input('Введите адрес электронной почты: ')
        check = bool(re.match(email_pattern, user_email))

        if check:
            print('Электронная почта принята')
            user_data_list.append(user_email)
            break
        else:
            print('Вы ввели неверный адрес электронной почты! Попробуйте еще раз!')

    return user_data_list


def create_users_list() -> list[list]:
    """
    Создает матрицу: список содержащий списки - информацию о пользователе

    :return: None
    """
    users_list = []

    while len(users_list) < 3:

        user_info = set_user_info()

        if user_info not in users_list:
            users_list.append(user_info)

    print(f'матрица: {users_list}')





create_users_list()




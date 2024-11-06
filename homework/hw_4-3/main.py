import re
from utils import get_reg_data, reg_check


def set_user_data(question: str, reg_pattern_name: str, user_data_list: list, all_patterns_dict: dict, users_list: list) -> list:
    """ 

    :param question: текст запроса данных пользователя
    :param reg_pattern_name: название паттерна для проверки
    :param user_data_list: список данных пользователя
    :return:
    """
    while True:
        # Получаем данные пользователя
        user_data = input(question)
        # Выьираем нужный паттерн
        pattern = all_patterns_dict.get(reg_pattern_name)
        # Проверяем введенные данные
        check = reg_check(user_data, pattern, users_list)

        # Логика
        if check:
            print('Принято')
            user_data_list.append(user_data)
            return user_data_list
            break 
        else:
            print('Вы ввели неверные данные! Попробуйте еще раз...')


def start_answers():
    """ 
    Точка входа

    :return:
    """
    # Получеем все паттерны для регулярок
    all_patterns_dict = get_reg_data()

    questions_list = [
        'Введите имя: ',
        'Введите фамилию: ',
        'Введите номер телефона: ',
        'Введите электронную почту: '
    ]

    pattern_names_list = [
        'name_pattern',
        'name_pattern',
        'phone_pattern',
        'email_pattern'
    ] 

    
    users_list = []
    user_data_list = []

    while len(users_list) < 3:
        
        for i in range(0, 4):
            result = set_user_data(
                questions_list[i], 
                pattern_names_list[i], 
                user_data_list, 
                all_patterns_dict,
                users_list
            )
            print(result)
            
        users_list.append(user_data_list)
        user_data_list = []


    print(users_list)



start_answers()
print('ciao')

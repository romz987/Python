def get_reg_data() -> list:
    """
    Возвращает список паттернов регулярных выражений
    для проверки пользовательских данных

    :return: список паттернов
    """
    patterns_list = [
        'pattern-one',
        'pattern-two',
        'pattern-three'
    ]

    return patterns_list


def reg_check(user_data: str, reg_pattern: str, users_list: list, data_to_check=None) -> str:
    """ 
    Возвращает аргумент user_data, если он прошел все 
    проверки

    :param user_data: пользовательские данные для проверки
    :param reg_pattern: паттерн регулярки для проверки данных
    :param users_list: список уже созданных пользователей
    :data_to_check:
    :return: user_data
    """
    pass 


def check_unique_data(user_data: str, ):
    """ 
    Проверяет уникальность введенного номера телефона 
    и адреса email

    :param user_data: пользовательские данные для проверки
    :param 
    """
    pass

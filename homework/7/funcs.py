import os 
import json


def get_user_level(level: str, questions: list) -> dict:
    """ 
    Принимает уровень сложности и возвращает 
    соответствующий словарь

    :param level: уровень сложности:
        'easy'    - легкий
        'medium'  - средний
        'hard'    - сложный
    :return: словарь для теста по английскому
    """
    if level == 'easy':
        return questions[0]
    elif level == 'medium':
        return questions[1]
    else:
        return questions[2]


def base_program(check_dictionary: dict) -> dict:
    """
    Задает вопросы по списку слов в переданном словаре

    :param check_dictionary: словарь с вопросами
    :return: результирующий словарь
    """
    answers = {}
    for key, value in check_dictionary.items():
        user_answer = str(
            input(f'Как переводится "{key}"?: ').lower().strip()
        )
        if user_answer == value:
            print('Правильно, братишка, одобряю!')
            answers[key] = True
        else:
            print('Неправда!')
            answers[key] = False 

    return answers


def get_result(results_dictionary: dict, user_answers_dictionary: dict):
    """ 
    Выводит правильно и неправильно отвеченные слова 
    и показатель уровня знаний

    :param result_dictionary: 
    :param user_answers_dictionary: 
    :return: 
    """
    score = 0
    right = []
    wrong = []
    result = ''
    for key, value in user_answers_dictionary.items():
        if value:
            score += 1
            right.append(key)
        else:
            wrong.append(key)

    for key, value in results_dictionary.items():
        if key == str(score):
            result = value

    print(f'\nПравильно отвеченные слова: {right}\n')
    print(f'Неправильно отвеченные слова: {wrong}\n')
    print(f'Ваш уровень: {result}')


def save_results(user_answers_dictionary: dict, username: str):
    """ 
    Сохраняем результаты в папку results 

    :param user_answers_dictionary: словарь с результатами
    :param username: имя пользователя
    :return: None
    """
    file_path= os.path.join('results', f'{username}.json')

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(user_answers_dictionary, file, ensure_ascii=False, indent=4)

    print('Результаты сохранены')

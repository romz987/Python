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
    if user_level == 'easy':
        return questions[0]
    elif user_level == 'medium':
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



if __name__ == "__main__":
    try:
        with open('questions.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
    except Exception as e:
        print(f'error: {str(e)}')

    questions = data[0]['questions']
    results_dictionary = data[1]['levels']

    while True:
        user_level = str(
            input('Введите уровень сложности [easy/medium/hard]: ')
        ).lower().strip()

        if user_level in ['easy', 'medium', 'hard']:
            break 
        else:
            print(f'{user_level} - недопустимое значение')

    check_dictionary = get_user_level(user_level, questions)
    user_answers_dictionary = base_program(check_dictionary)
    get_result(results_dictionary, user_answers_dictionary)

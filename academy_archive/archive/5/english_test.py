from typing import Literal


def get_dictionary(dictionary_level: Literal['easy', 'medium', 'hard']) -> dict:
    """  
    Набор словарей различных уровней сложности.

    :param dictionary_level: уровень сложности:
        'easy'   - легкий
        'medium' - средний
        'hard'   - сложный
    :return: словарь
    """
    dictionaries = {
        'easy': {
            "family": "семья",
            "hand": "рука",
            "people": "люди",
            "evening": "вечер",
            "minute": "минута",
        },
        'medium': {
            "believe": "верить",
            "feel": "чувствовать",
            "make": "делать",
            "open": "открывать",
            "think": "думать",
        },
        'hard': {
            "rural": "деревенский",
            "fortune": "удача",
            "exercise": "упражнение",
            "suggest": "предлагать",
            "except": "кроме",
        }
    }

    if dictionary_level in dictionaries:
        return dictionaries[dictionary_level]
    else:
        return


def ask_level() -> dict:
    """ 
    Запрос уровня сложности 

    :return: словарь
    """
    user_level = str(
        input('Введите уровень сложности [easy/medium/hard]: ')
    ).lower().strip()

    words = get_dictionary(user_level)
    if words is None:
        print(f'{user_level} - недопустимое значение')
        ask_level()
    else:
        return words


def show_results(answers: dict):
    """ 
    Показывает правильно отвеченные слова 

    :param answers: словарь True-False
    :return: None
    """
    print('Правильно отвеченные слова:')
    for key, value in answers.items():
        if value: 
            print(key)

    print('\nНеправильно отвеченные слова:')
    for key, value in answers.items():
        if value is False:
            print(key)


def show_level(answers: dict):
    """  
    Показывает уровень согласно условиям

    :param answers: словарь True-False
    :return: None
    """
    counter = 0
    for key, value in answers.items():
        if value:
            counter += 1

    levels = {
        0: "Нулевой",
        1: "Так себе",
        2: "Можно лучше",
        3: "Норм",
        4: "Хорошо",
        5: "Отлично"
    }
   
    print(f'\n\nВаш ранг:\n{levels[counter]}')


def start():
    """ Точка входа """
    words = ask_level()
    answers = {}

    for key, value in words.items():
        print(
            f'{key} - {len(value)} букв, начинается на "{value[0]}"...'
        )
        user_answer = str(
            input('Как переводится это слово?: ')
        ).lower().strip()
        if user_answer == value:
            print(f'Верно, {key.title()} - это {user_answer}.\n')
            answers[key] = True
        else: 
            print(f'Неверно! {key.title()} - это {value}.\n')
            answers[key] = False

    show_results(answers)
    show_level(answers)



start()

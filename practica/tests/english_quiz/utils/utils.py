import json


def get_data(filename):
    with open(filename, encoding='utf-8') as file:
        json_data = file.read()
        python_data = json.loads(json_data)
    return python_data


def get_quiz_words(level, questions_list):
    if level == 'средний':
        quiz_words = questions_list[1]
    elif level == 'сложный':
        quiz_words = questions_list[2]
    else:
        quiz_words = questions_list[0]
    return quiz_words


def base_program(quiz_words):
    answers = {}
    for word, translate in quiz_words.items():
        answer = input(f'\n{word}, {len(translate)} букв, начинается на {translate[0].title()}...\n').strip().lower()

        if answer == translate:
            print(f"Верно, {word.title()} это {translate.title()}")
            answers[word] = True
        else:
            print(f"Неверно, {word.title()} это {translate.title()}")
            answers[word] = False
    return answers


def get_result(answers, knowledge_level):
    counter = 0
    print('\nПравильно отвечены слова:')
    for key, value in answers.items():
        if value is True:
            print(key)
            counter += 1
    print('\nНеправильно отвечены слова:')
    for key, value in answers.items():
        if value is False:
            print(key)
    return knowledge_level[str(counter)]


def write_answers(filename, answers):
    answers_json = json.dumps(answers, ensure_ascii=False, indent=4)
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(answers_json)
    return f'Данные записаны в {filename}!'

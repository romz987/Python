from utils.utils import get_data, get_quiz_words, base_program, get_result, write_answers

if __name__ == '__main__':

    try:
        questions, levels = get_data(r'questions_data/questions.json')
    except FileNotFoundError:
        print('Файл не найден!!')
        exit()
    questions_list = questions['questions']
    knowledge_level = levels['levels']
    user_name = input("Введите ваше имя: ")
    if not user_name.isalnum():
        print('Недопустимое имя!')
        exit()
    user_level = input('Введите уровень сложности легкий/средний/сложный: ')
    user_quiz_words = get_quiz_words(user_level, questions_list)
    user_answers = base_program(user_quiz_words)
    user_result = get_result(user_answers, knowledge_level)
    print(f'\nВаш ранг:\n{user_result}')
    try:
        print(write_answers(fr'students_data/{user_name}_answers.json', user_answers))
    except FileNotFoundError:
        print('Директория для записи не найдена!!!')
        exit()

import json 
from funcs import * 


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
            username = str(
                input('Как Вас зовут?: ')
            )
            break 
        else:
            print(f'{user_level} - недопустимое значение')

    check_dictionary = get_user_level(user_level, questions)
    user_answers_dictionary = base_program(check_dictionary)
    get_result(results_dictionary, user_answers_dictionary)
    save_results(user_answers_dictionary, username)




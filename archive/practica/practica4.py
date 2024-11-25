import json

def create_dict(list_one, list_two):
    result_dict = {}
    for i in range(0, len(list_one)):
        key = list_one[i]
        value = list_two[i]
        result_dict[key] = value 

    return result_dict


def save_result(result):
    with open('result.json', 'w', encoding='UTF-8') as file:
        json.dump(result, file, indent=2, ensure_ascii=False)


def show_json_content():
    with open('result.json', 'r', encoding='UTF-8') as file:
        result = json.load(file)
        print(result)

    for key, value in result.items():
        print(f'{key} - это {value}')


# list_one = ['cat', 'dog', 'bird', 'lizard']
# list_two = ['кошка', 'собака', 'птица', 'ящерица']
#
# result = create_dict(list_one, list_two)

show_json_content()

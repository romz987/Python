import os 


def normalized_path() -> str:
    """ Нормализованный путь до файла test_file_1.txt"""
    relative_path = 'data_path_1/test_file_1.txt'
    normal_path = os.path.abspath(relative_path)

    return normal_path 


def directory_walk():
    """Обходим текущую директорию"""
    directory = '.'
    # Обходим директорию
    for dirpath, dirnames, filenames in os.walk(directory):
        print(f'Текущий каталог: {dirpath}')
        print('Подкаталоги:', dirnames)
        print('Файлы:', filenames)
        print()


def get_normalized_path() -> str:
    """Составляет нормализованный абсолютный путь к test_file_3"""
    # Указываем директорию, в которой находится файл
    directory = 'data_path_2'
    # Составляем нормализованный абсолютный путь
    normalized_path = os.path.abspath(os.path.join(directory, 'test_file_3'))
    return normalized_path


def create_directory(dir_name: str) -> None:
    """Создает папку с указанным именем внутри data_path_2"""
    directory = 'data_path_2'
    path = os.path.join(directory, dir_name)
    try:
        os.makedirs(path)  # Создает директорию, включая все промежуточные директории
        print(f'Папка "{dir_name}" успешно создана в "{directory}".')
    except FileExistsError:
        print(f'Папка "{dir_name}" уже существует в "{directory}".')
    except Exception as e:
        print(f'Ошибка при создании папки: {e}')


def remove_directory(dir_name: str) -> None:
    """Удаляет папку с указанным именем внутри data_path_2"""
    directory = 'data_path_2'
    path = os.path.join(directory, dir_name)
    try:
        os.rmdir(path)  # Удаляет директорию (должна быть пустой)
        print(f'Папка "{dir_name}" успешно удалена из "{directory}".')
    except FileNotFoundError:
        print(f'Папка "{dir_name}" не найдена в "{directory}".')
    except OSError:
        print(f'Ошибка: Папка "{dir_name}" не пуста или не может быть удалена.')
    except Exception as e:
        print(f'Ошибка при удалении папки: {e}')


def write_text_to_file(filename: str, text: str) -> None:
    """Записывает указанный текст в файл построчно."""
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)


def read_text_from_file(filename: str) -> None:
    """Читает текст из файла и выводит его в консоль построчно."""
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')


# Задание 1-1
# Нормализваонный путь 
normal_path = normalized_path()
print(
    f'Нормализованный путь до test_file_1.txt: {normal_path}'
)

# Задание 1-2
# os walk
directory_walk()

# Задание 1-3
path = get_normalized_path()
print(
    f'Нормализованный путь до test_file_3.txt: {normal_path}'
)

# Задание 1-4
create_directory('new_dir')
remove_directory('new_dir')


# Задание 2
# Текст для записи
text_to_write = """Если б мишки были пчелами,
То они бы нипочем,
Никогда и не подумали,
Так высоко строить дом."""

# Записываем текст в файл test_file_1.txt
write_text_to_file('data_path_1/test_file_1.txt', text_to_write)

# Читаем текст из файла test_file_1.txt
print('\n\n')
read_text_from_file('data_path_1/test_file_1.txt')

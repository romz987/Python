cinema_genres = ("Комедия", "Экшн", "Пеплум", "Триллер")


def change_genre(_tuple: tuple, name_one: str, name_two: str) -> tuple:
    """ 
    Заменить любой элемент кортежа

    :param tuple: кортеж
    :param name_one: что заменить
    :param name_two: на что заменить
    :return: новый кортеж
    """
    _list = []
    for i in _tuple:
        if i == name_one:
            i = name_two 

        _list.append(i) 

    _tuple = tuple(_list)
    print(_tuple)
    return _tuple


def add_genre_in_place(_tuple: tuple, name_one: str) -> tuple:
    """ 
    Добавляет новый жанр между жанрами боевик и пеплум 

    :param tuple: кортеж
    :param name_one: что добавить
    :return: новый кортеж
    """
    _list = []
    for i in _tuple:
        if i == 'Пеплум':
            _list.append(name_one)

        _list.append(i) 

    _tuple = tuple(_list)
    print(_tuple)
    return _tuple




new_cinema_genres = change_genre(cinema_genres, 'Экшн', 'Боевик')
long_cinema_genres = add_genre_in_place(new_cinema_genres, 'Фэнтези')

long_cinema_genres = ', '.join(long_cinema_genres)
print(f'Обновленные жанры кино: {long_cinema_genres}')


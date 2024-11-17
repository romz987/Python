import random


cinema_genres = [
    "комедия", 
    "экшн", 
    "пеплум", 
    "триллер", 
    "комедия", 
    "пеплум"
]

# список в множество
genres_set = set(cinema_genres)

# добавляем 2 жанра 
genres_set.add("драма")
genres_set.add("фантастика")

# Удаляем жанр
genres_set.remove("экшн")

# Удаляем случайный жанр
random_genre = random.choice(list(genres_set))
genres_set.remove(random_genre)

updated_genres_list = list(genres_set)


print("Обновленный список жанров:", updated_genres_list)


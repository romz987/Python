# Мои вещи
my_items = {
    "палатка",
    "еда", 
    "вода", 
    "фонарик", 
    "нож", 
    "аптечка", 
    "карта", 
    "компас", 
    "спички", 
    "книга"
}

# Вещи друга
friend_items = {
    "палатка", 
    "еда", 
    "вода", 
    "книга", 
    "одежда", 
    "фотоаппарат", 
    "спички", 
    "солнцезащитный крем", 
    "фляга", 
    "надувная лодка"
}

# Вещи котороые взяли мы оба
common_items = my_items.intersection(friend_items)

# Вещи которые взял только я
only_my_items = my_items.difference(friend_items)

# Вещи которые возьмет только друг
only_friend_items = friend_items.difference(my_items)

# Вещи которые есть и нас обоих
all_items = my_items.union(friend_items)

print("Вещи, которые взяли мы оба:", common_items)
print("Вещи, которые взял только я:", only_my_items)
print("Вещи, которые возьмет друг:", only_friend_items)
print("Все вещи, которые мы взяли:", all_items)


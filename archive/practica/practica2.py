cars = (
    'VAZ',
    'Toyota',
    'Audi',
    'GAZ',
    'VAZ',
    'MAZ',
    'Audi'
)

car_name = input('Введите марку, которую надо заменить: ')
new_car_name = input('Введите на что заменить: ')

cars_list = list(cars)

for i in range(0, len(cars_list)):
    if cars_list[i] == car_name:
        cars_list[i] = new_car_name

cars = tuple(cars_list)
print(cars)

print('buy')

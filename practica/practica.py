def show_quote():
    name = 'Steve Jobs'

    print(
        'Don\'t let the noise of others opinions\n' 
        'drown out your own inner voice\n'
        f'{name.rjust(40)}'
    )


def odd_numbers(num_one: int, num_two: int):
    if num_one > num_two:
        num_one, num_two = num_two, num_one 

    for i in range(num_one, num_two + 1):
        if i % 2 != 0:
            print(i)


odd_numbers(20, 10)


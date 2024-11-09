# Примеры использования *args и **kwargs
def args_example(*args):
    """ args example """
    print(args)

    for arg in args:
        print(arg)


def kwargs_example(**kwargs):
    """ kwargs example """
    for key, value in kwargs.items():
        print(
            f'key is: {key}'
            f'\tvalue is: {value}'
        )



args_example(1, 5, 8, 'g', 'm')

kwargs_example(animal='cat', mask='ilon', president='trump')

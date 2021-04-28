from functools import reduce

new_list = [x for x in range(100, 1001, 2)]
print(new_list)


def my_func(x, y):
    """ Возвращает произведение двух чисел. """
    return x * y


print(reduce(my_func, new_list))
input('\nPress ENTER to exit')

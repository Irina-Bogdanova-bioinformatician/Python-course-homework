from math import factorial


def my_generator(m):
    """ Возвращает объект-генератор, генерирующий факториалы чисел от 1 до n.

    Вводимый пользователем параметр - целое число(int).

    """
    for i in range(1, m+1):
        yield factorial(i)


n = int(input("Введите целое положительное число "))
g = my_generator(n)
for a in g:
    print(a)
input('\nPress ENTER to exit')

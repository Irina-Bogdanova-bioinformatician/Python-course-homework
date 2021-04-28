def my_generator(m):
    """ Возвращает объект-генератор, генерирующий факториалы чисел от 1 до n.

    Вводимый пользователем параметр - целое число(int).

    """
    for i in range(1, m + 1):
        b = 1
        for c in range(1, i + 1):
            b = b * c
        yield b


n = int(input("Введите число целое положительное число "))
g = my_generator(n)
for a in g:
    print(a)
input('\nPress ENTER to exit')

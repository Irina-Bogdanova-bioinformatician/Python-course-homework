def my_func():
    """ Принимает три аргумента и возвращает сумму наибольших двух аргументов.

    Использует встроенные функции map(), float(), input(), min(), sum() и методы .remove(x), .split("").
    Позиционные параметры:
    num_1, num_2, num_3 -- вводимые пользователем аргументы в виде строки(str).
    Программа возвращает число типа float.

    """
    num_1, num_2, num_3 = map(float, input("Введите три числа через запятую ").split(","))
    num_list = [num_1, num_2, num_3]
    a = min(num_list)
    num_list.remove(a)
    return f'Сумма наибольших двух из чисел равна {sum(num_list)}'


print(my_func())
input('\nPress ENTER to exit')

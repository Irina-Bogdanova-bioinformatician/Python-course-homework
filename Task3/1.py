def division_culc():
    """ Возвращает частное от деления. В случае деления на ноль возвращает строку "На ноль делить нельзя".

    Использует встроенные функции float(), map(), input() и метод .split("").
    Позиционные параметры (значения вводит пользователь):
    dividend -- делимое (float)
    divider -- делитель (float)
    Программа выводит число типа float.

    """
    dividend, divider = map(float, input("Введите делимое и делитель через запятую ").split(","))
    if divider == 0:
        return "На ноль делить нельзя"
    else:
        return f"Частное равно {dividend / divider}"


print(division_culc())
input('\nPress ENTER to exit')

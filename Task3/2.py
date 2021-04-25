def user_information():
    """ Возвращает данные пользователя одной строкой.

    Использует встроенную функцию input().
    Именованные параметры (значения вводит пользователь):
    name -- имя (str)
    surname -- фамилия (str)
    year_of_birth -- год рождения (str)
    city -- город проживания (str)
    email -- адрес электронной почты (str)
    phone_number -- номер телефона (str)

    """
    name = input("Введите имя ")
    surname = input("Введите фамилию ")
    year_of_birth = input("Введите год рождения ")
    city = input("Введите город проживания ")
    email = input("Введите email ")
    phone_number = input("Введите номер телефона ")
    return f"Имя: {name}, фамилия: {surname}, год рождения: {year_of_birth}," \
           f" город проживания: {city}, email: {email}, номер телефона: {phone_number}."


print(user_information())
input('\nPress ENTER to exit')

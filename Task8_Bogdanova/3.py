import re


class OwnError(Exception):
    def __init__(self, message):
        self.message = message


numbers_list = []
while "stop" not in numbers_list:
    new_number = input("Введите число. Для завершения работы программы введите stop. ")
    try:
        if re.match(r'\D', new_number):
            if new_number == "stop":
                print(f"Работа программы завершена. Список введенных чисел: {numbers_list}")
                break
            else:
                raise OwnError("Вы ввели не число!")
        numbers_list.append(new_number)
    except OwnError as err:
        print(err)
    else:
        print(numbers_list)

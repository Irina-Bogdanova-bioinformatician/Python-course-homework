class OwnError(Exception):
    def __init__(self, message):
        self.message = message


try:
    dividend_number = float(input("Введите делимое "))
    divisor_number = float(input("Введите делитель "))
    if divisor_number == 0:
        raise OwnError("Делить на ноль нельзя!")
except ValueError:
    print("Вы ввели не число.")
except OwnError as err:
    print(err)
else:
    print(dividend_number / divisor_number)

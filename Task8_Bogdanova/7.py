import re


class ComplexNumber:
    def __init__(self, new_number):
        self.new_number = re.sub(r"[\s*]", "", new_number)
        if "j" not in self.new_number:
            print(f"Введите символ j для обозначения мнимой единицы в числе {self.new_number}.")
        else:
            try:
                self.final_number = complex(self.new_number)
            except ValueError:
                print(f"Неверный формат комплексного числа {self.new_number}.")

    def __add__(self, other):
        try:
            sum_number = self.final_number + other.final_number
            return f"Сумма введенных комплексных чисел равна {sum_number}"
        except AttributeError:
            return f"Пожалуйста, исправьте формат указанных чисел для совершения операции сложения."

    def __mul__(self, other):
        try:
            sum_number = self.final_number * other.final_number
            return f"Произведение введенных комплексных чисел равно {sum_number}"
        except AttributeError:
            return f"Пожалуйста, исправьте формат указанных чисел(числа) для совершения операции умножения."


a = ComplexNumber("3 + 4*j")
b = ComplexNumber("1e3 + 2e-3j")
c = ComplexNumber(".1-2.j")
print(a + b)
print(a * b)
print(a + c)
d = ComplexNumber("3 + 4*i")
print(d + c)

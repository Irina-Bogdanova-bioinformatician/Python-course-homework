import re


class Date:
    @classmethod
    def convert_to_number(cls, date):
        if Date.validate(date) == "Валидация прошла успешно.":
            date_list = date.split("-")
            date_list_new = [int(x) for x in date_list]
            day, month, year = date_list_new
            return f'{day:02d}-{month:02d}-{year:04d}'
        else:
            return Date.validate(date)

    @staticmethod
    def validate(date):
        date_list = date.split("-")
        date_string = "".join(date_list)
        error_list = []
        for el in date_string:
            if re.match(r'\D', el):
                error_list += el
            else:
                continue
        if len(error_list) != 0:
            return "Неверный формат даты. Присутствуют посторонние символы."
        else:
            date_list_new = [int(x) for x in date_list if x != ""]
            if len(date_list_new) != 3:
                return "Неверный формат даты. Присутствуют лишние цифры."
            else:
                day, month, year = date_list_new
                if year > 2100:
                    return "Неверный формат даты. Год не должен быть больше 2100."
                if month > 12 or month == 0:
                    return "Неверный формат даты. Месяц должен находиться в диапазоне от 1 до 12 включительно."
                if day == 0:
                    return "Неверный формат даты. Количество дней в месяце должно быть больше 0."
                else:
                    if (month in [1, 3, 5, 7, 8, 10, 12] and day > 31) or (month in [4, 6, 9, 11] and day > 30):
                        return "Неверный формат даты. Количество дней в месяце превышает допустимое."
                    elif month == 2:
                        if (year % 4 == 0 and day > 29) or (year % 4 != 0 and day > 28):
                            return "Неверный формат даты. Количество дней в месяце превышает допустимое."
                        else:
                            return 'Валидация прошла успешно.'
                    else:
                        return 'Валидация прошла успешно.'


print(Date.validate("01-05-1991"))
print(Date.validate("0-23-4-05-1991"))
print(Date.validate("29-02-2000"))
print(Date.validate("29-02-2001"))
print(Date.validate("01-13-1995"))
print(Date.validate("00-05-1991"))
print(Date.validate("04-00-1991"))
print(Date.validate("04-06-2101"))
print(Date.convert_to_number("01-05-1991"))
print(Date.convert_to_number("04-00-1991"))
print(Date.convert_to_number("29-02-2004"))
print(Date.convert_to_number("01-05-1991"))

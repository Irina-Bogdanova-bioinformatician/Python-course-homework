class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)
        pass

    def get_full_name(self):
        return f"Полное имя сотрудника: {self.surname} {self.name}."

    def get_total_income(self):
        _total_income = 0
        for value in self._income.values():
            _total_income += value
        return f"Доход с учётом премии: {_total_income}."


a = Position("Иван", "Иванов", "Курьер", 40000, 5000)
print(a.get_full_name(), a.get_total_income())
print(a.name, a.surname, a.position, a._income)
b = Position("Алина", "Зайцева", "Менеджер", 70000, 10000)
print(b.get_full_name(), b.get_total_income())
print(b.name, b.surname, b.position, b._income)

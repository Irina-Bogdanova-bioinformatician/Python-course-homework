class Cell:
    def __init__(self, cells_number):
        self.cells_number = int(cells_number)

    def __add__(self, other):
        return Cell(self.cells_number + other.cells_number)

    def __sub__(self, other):
        residual = self.cells_number - other.cells_number
        if residual > 0:
            return Cell(self.cells_number - other.cells_number)
        elif residual == 0:
            return "Клетки содержат равное количество ячеек"
        else:
            return "Уменьшаемая клетка меньше вычитаемой "

    def __mul__(self, other):
        return Cell(self.cells_number * other.cells_number)

    def __truediv__(self, other):
        return Cell(self.cells_number // other.cells_number)

    def __str__(self):
        return f"Создана новая клетка с числом ячеек, равным {self.cells_number}"

    def make_order(self, row):
        row = int(row)
        counter = self.cells_number
        final_string = ""
        while counter > 0:
            if counter // row > 0:
                final_string += "*" * row
                final_string += "\n"
                counter -= row
            else:
                final_string += "*" * counter
                break
        if self.cells_number % row == 0:
            return final_string[:-1]
        else:
            return final_string


a = Cell(10)
b = Cell(5)
print(a - b)
print(a + b)
print(a / b)
print(a * b)
print(a.make_order(3))
c = a + b
print(c)
print(c.make_order(5))

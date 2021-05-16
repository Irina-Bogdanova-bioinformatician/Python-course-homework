class Matrix:
    def __init__(self, new_matrix):
        self.new_matrix = new_matrix

    def __str__(self):
        final_matrix = ""
        for line in self.new_matrix:
            modified_line = [str(el) for el in line]
            new_line = " ".join(modified_line)
            final_matrix = final_matrix + new_line + "\n"
        return final_matrix

    def __add__(self, other):
        sum_matrix = []
        line_sum_matrix = []
        for c, d in zip(self.new_matrix, other.new_matrix):
            for e, f in zip(c, d):
                line_sum_matrix.append(e + f)
            sum_matrix += [line_sum_matrix]
            line_sum_matrix = []
        return Matrix(sum_matrix)


a = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a)
b = Matrix([[2, 3, 4], [5, 6, 7], [8, 8, 8]])
print(b)
print(a+b)

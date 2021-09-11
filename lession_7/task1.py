class Matrix:
    matrix_list = []

    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __str__(self):
        result = []
        for row in self.matrix_list:
            row_string = ' '.join(str(x) for x in row)
            result.append(row_string)
        return '\n'.join(result)

    def __add__(self, matrix):
        result = []

        self_row_len = len(self.matrix_list)
        other_row_len = len(matrix.matrix_list)

        if self_row_len != other_row_len:
            raise Exception("Не могу сложить матрицы разного размера")

        row_index = 0
        while row_index < self_row_len:
            row_result = []

            self_row = self.matrix_list[row_index]
            other_row = matrix.matrix_list[row_index]
            if len(self_row) != len(other_row):
                raise Exception("Не могу сложить матрицы разного размера")

            col_index = 0
            while col_index < len(self_row):
                row_result.append(self_row[col_index] + other_row[col_index])
                col_index += 1

            row_index += 1
            result.append(row_result)

        return Matrix(result)


def task_1():
    a = Matrix([[1, 2, 3], [3, 4, 5]])
    b = Matrix([[2, 3, 4], [4, 5, 6]])
    c = a + b
    print(c)

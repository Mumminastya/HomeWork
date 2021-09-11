class Cell:
    N = 0

    def __init__(self, n):
        self.N = n

    def __add__(self, other):
        return Cell(self.N + other.N)

    def __sub__(self, other):
        if self.N >= other.N:
            return Cell(self.N - other.N)
        raise Exception("Не могу вычитать")

    def __mul__(self, other):
        return Cell(self.N * other.N)

    def __truediv__(self, other):
        if other.N == 0:
            raise ZeroDivisionError("Не могу делить на 0")
        return Cell(int(self.N / other.N))

    def __str__(self):
        return str(self.N)

    def make_order(self, p):
        a = self.N // p
        b = self.N % p
        full_string = "*" * p + "\n"
        full_string = full_string * a
        short_string = "*" * b
        if len(short_string) == 0:
            return full_string.rstrip('\n')
        else:
            return full_string + short_string


def task_3():
    a = Cell(6)
    b = Cell(5)

    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(a.make_order(2))
    print(b.make_order(2))

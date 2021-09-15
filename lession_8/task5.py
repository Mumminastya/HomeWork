class Complex:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def __add__(self, other):
        a = self.a + other.a
        b = self.b + other.b
        return Complex(a, b)

    def __mul__(self, other):
        a = (self.a * other.a - self.b * other.b)
        b = (self.b * other.a + self.a * other.b)
        return Complex(a, b)

    def __str__(self):
        return f"{self.a}+{self.b}*i"


def task_5():
    c1 = Complex(1, 2)
    c2 = Complex(2, 3)
    c3 = c1 + c2
    c4 = c1 * c2
    print(c3)
    print(c4)

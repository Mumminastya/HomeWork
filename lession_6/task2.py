class Road:
    _lenght = 0
    _width = 0

    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width

    def calc(self, weight, thickness):
        return self._lenght * self._width * weight * thickness

def task_2():
    a = Road(1, 2)
    b = a.calc(1, 50)
    print(b)


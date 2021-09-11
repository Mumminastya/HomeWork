from abc import ABC, abstractmethod


class Clothes(ABC):
    @property
    @abstractmethod
    def calc(self):
        pass


class Coat(Clothes):
    V: 0

    def __init__(self, v):
        self.V = v

    @property
    def calc(self):
        return self.V/6.5 + 0.5


class Suit(Clothes):
    H: 0

    def __init__(self, h):
        self.H = h

    @property
    def calc(self):
        return 2 * self.H + 0.3


def task_2():
    a = Coat(65)
    b = Suit(6)
    clot = [a, b]
    for c in clot:
        print(c.calc)


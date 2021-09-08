class Worker:
    name = ""
    surname = ""
    position = ""
    _income_elem = {"wage": 0, "bonus": 0}

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income_elem["wage"] = wage
        self._income_elem["bonus"] = bonus


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income_elem["wage"] + self._income_elem["bonus"]


def task_3():
    a = Position("Tom", "Hanks", "actor", 10, 1000000)
    b = a.get_full_name()
    c = a.get_total_income()
    print(b)
    print(c)

from abc import ABC


class OfficeTech(ABC):
    serial_number: str
    place: str
    title: str


class Storage:

    def __init__(self):
        self.main_storage = {}

    def add_tech(self, tech: OfficeTech):
        self.main_storage.setdefault(type(tech).__name__, []).append(tech)

    @classmethod
    def move(cls, st1, st2, tech_type, count):
        tech_type_name = tech_type.__name__
        print(tech_type_name)
        if not (tech_type_name in st1.main_storage):
            raise Exception("Не достаточно техники")

        if len(st1.main_storage[tech_type_name]) < count:
            raise Exception("Не достаточно техники")

        while count > 0:
            current_tech = st1.main_storage[tech_type_name].pop(0)
            st2.add_tech(current_tech)
            count -= 1


class Printer(OfficeTech):
    format: str


class Fax(OfficeTech):
    number: str


def task_4():
    pr1 = Printer()
    pr1.title = "Пр1"

    pr2 = Printer()
    pr1.title = "Пр2"

    f1 = Fax()
    f1.title = "Ф1"

    storage = Storage()
    storage.add_tech(pr1)
    storage.add_tech(pr2)
    storage.add_tech(f1)

    buh_storage = Storage()
    Storage.move(storage, buh_storage, Fax, 1)
    print(buh_storage.main_storage)
    print(storage.main_storage)

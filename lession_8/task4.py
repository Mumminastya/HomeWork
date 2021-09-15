from abc import ABC


class OfficeTech(ABC):
    def __init__(self, serial_number: str, place: str, title: str):
        self.serial_number = serial_number
        self.place = place
        self.title = title


class Storage:

    def __init__(self):
        self.main_storage = {}

    def add_tech(self, tech: OfficeTech):
        self.main_storage.setdefault(type(tech).__name__, []).append(tech)

    @classmethod
    def move(cls, st1, st2, tech_type, count):
        if not (count.isnumeric()):
            raise Exception("Количество должно быть числом")

        tech_type_name = tech_type.__name__
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
    storage = Storage()
    buh_storage = Storage()
    while True:
        operation = input("Выберите операцию (Add-1/Move-2/Stop=3): ")
        if not (operation.isnumeric()):
            print("Only 1/2 available")
            continue
        match operation:
            case 1:
                tech_type = input("Выберите тип техники (Printer-P/Fax-F): ")
                match tech_type:
                    case "P":
                        p = Printer()
                        storage.add_tech(p)
                    case "F":
                        f = Fax()
                        storage.add_tech(p)
                    case _:
                        print("Tech type not found")
                        continue
            case 2:
                tech_type = input("Выберите тип техники (Printer-P/Fax-F): ")
                match tech_type:
                    case "P":
                        Storage.move(storage, buh_storage, Printer, 1)
                    case "F":
                        Storage.move(storage, buh_storage, Fax, 1)
                    case _:
                        print("Tech type not found")
                        continue
            case 3:
                break
            case _:
                print("Only 1/2 available")
                continue

    print(buh_storage.main_storage)
    print(storage.main_storage)

class Stationery:
    def __init__ (self, title):
        self.title = title

    def draw (self):
        print("I'm Stationary")


class Pen (Stationery):
    def draw(self):
        print(f"Take a {self.title}")


class Pencil (Stationery):
    def draw(self):
        print(f"Take a {self.title}")


class Handle (Stationery):
    def draw(self):
        print(f"Take a {self.title}")


def task_5():
    pen = Pen("Pen")
    pen.draw()
    pencil = Pencil("Pencil")
    pencil.draw()
    handle = Handle("Handle")
    handle.draw()

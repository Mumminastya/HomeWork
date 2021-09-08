class Car:
    speed = 0
    color = ""
    name = ""
    is_police = False

    def go(self):
        print(f"{self.name} Go!")

    def stop_method (self):
        print(f"{self.name} Stop!")

    def turn (self, direction):
        print(f"Car turn {direction}")

    def show_speed (self):
        print(self.speed)


class TownCar (Car):
    def show_speed(self):
        print(self.speed)
        if self.speed > 60:
            print(f"{self.name}! Превышение скорости!")


class WorkCar(Car):
    def show_speed(self):
        print(self.speed)
        if self.speed > 40:
            print(f"{self.name}! Превышение скорости!")

class PoliceCar(Car):
    def __init__(self):
        self.is_police = True


class SportCar (Car):
    pass

def task_4():
    a = TownCar()
    a.name = "Василий"
    a.color = "red"
    a.speed = 61
    a.show_speed()
    a.turn("Left")

    b = SportCar()
    b.name = "Михаил"
    b.color = "yellow"
    b.speed = 561
    b.show_speed()
    b.turn("Up")

    b = WorkCar()
    b.name = "Николай"
    b.color = "blue"
    b.speed = 61
    b.show_speed()
    b.turn("Right")

    c = PoliceCar()
    c.name = "Григорий"
    c.color = "black"
    c.speed = 160
    c.go()
    c.turn("Underground")


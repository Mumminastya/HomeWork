from time import sleep


class TrafficLight:
    __color = ""
    __colors = {1: "Red", 2: "Yellow", 3: "Green"}
    __colors_map = {1: 2, 2: 3, 3: 1}
    __colors_times = {1: 7, 2: 2, 3: 3}
    __current_color = 1

    def running(self):
        while 1 == 1:
            self.__color = self.__colors[self.__current_color]
            print(self.__color)
            sleep(self.__colors_times[self.__current_color])
            self.__current_color = self.__colors_map[self.__current_color]


def task_1():
    a = TrafficLight()
    a.running()

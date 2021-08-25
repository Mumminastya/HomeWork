def my_func(boom_1, boom_2, boom_3):
    boom = [boom_1, boom_2, boom_3]
    boom.sort(reverse=1)
    return boom[0] + boom[1]


def task_3():
    boom_1 = int(input("Первое число: "))
    boom_2 = int(input("Второе число: "))
    boom_3 = int(input("Третье число: "))
    result = my_func(boom_1, boom_2, boom_3)
    print(result)

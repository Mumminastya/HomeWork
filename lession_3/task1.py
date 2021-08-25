def my_func(num_1, num_2):
    if num_2 == 0:
        raise ValueError(f"num_2 not be equals 0")
    return num_1 / num_2


def task_1():
    num_1 = int(input("Введите num_1: "))
    num_2 = int(input("Введите num_2: "))
    result = my_func(num_1, num_2)
    print(result)
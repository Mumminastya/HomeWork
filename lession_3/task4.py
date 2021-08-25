def my_func(x, y):
    result = 1
    while y < 0:
        result = result / x
        y = y + 1
    return result


def task_4():
    x = float(input("Положительное число: "))
    y = int(input("Целое отрицательное число: "))
    result = my_func(x, y)
    print(result)

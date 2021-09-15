# define Python user-defined exceptions
class CustomZeroDivisionError(ZeroDivisionError):
    pass


def task_2():
    try:
        a = int(input("Введите a: "))
        b = int(input("Введите b: "))
        if b == 0:
            raise CustomZeroDivisionError()
        print(a/b)
    except ZeroDivisionError:
        print("Нельзя делить на 0")


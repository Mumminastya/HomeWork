# define Python user-defined exceptions
class OnlyNumber(Exception):
    pass


def check_stop(a):
    if a == "stop":
        return True
    if a.isnumeric() == False:
        raise OnlyNumber()
    return False

def task_3():
    result = []
    while True:
        a = input("Введите число: ")
        try:
            if check_stop(a):
                break
            result.append(int(a))
            print(result)
        except OnlyNumber:
            print("Только числа")
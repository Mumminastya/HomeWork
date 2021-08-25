def int_func(word):
    return word.title()


def task_6_7():
    hu = input("Введи слова через пробел: ")
    hu_mas = hu.split()
    index = 0
    while index < len(hu_mas):
        hu_mas[index] = int_func(hu_mas[index])
        index += 1
    result = " "
    result = result.join(hu_mas)
    print(result)
def task_5():
    result = 0
    stop = 0
    while 1 == 1:
        x = input("Введи строку чисел через пробел (стоп-слово red): ")
        summ = x.split()
        for elem in summ:
            if elem == "red":
                stop = 1
                break
            result = result + int(elem)
        print(result)
        if stop == 1:
            break

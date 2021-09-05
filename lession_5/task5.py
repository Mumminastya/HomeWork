import random

def task_5():

    with open('task5.txt', 'w') as file:
        for el in range(1, 11):
            file.write(f'{random.randint(0, 99)} ')

    with open('task5.txt', 'r') as file:
        line = file.readline()
        num_mas = line.split()
        result = 0
        for num in num_mas:
            result = result + int(num)
        print(result)
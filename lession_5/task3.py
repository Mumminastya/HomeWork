def task_3():
#Создать текстовый файл(не программно).Построчно записать фамилии сотрудников и величину
#их окладов(не менее 10 строк).Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии
# этих сотрудников.Выполнить подсчёт средней величины дохода сотрудников.
    with open('text_task3.txt', encoding = 'utf-8', mode='r') as file:
        line_index = 0
        total_sal = float(0)
        for line in file:
            words = line.split()
            sal = float(words[1])
            if sal < 20000:
                print(words[0])
            line_index = line_index + 1
            total_sal = total_sal + sal
        print(total_sal / line_index)
def task_2():
# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
    with open('text_task2.txt', 'r') as file:
        line_index = 1
        for line in file:
            words = line.split()
            print(f'{line_index} - {len(words)}')
            line_index = line_index + 1
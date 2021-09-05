def task_1():
# Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
    with open('test.txt', 'w') as file:
        while 1 == 1:
            user_text = input("Введите текст: ")
            if user_text == "":
                break
            user_text = f'{user_text}\n'
            file.write(user_text)
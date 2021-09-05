def task_4():
    with open('text_task4.txt', encoding='utf-8', mode='r') as file:
        with open('text_task4_result.txt', encoding='utf-8', mode='w') as file_result:
            rus_dig = {1:"Один", 2: "Два", 3: "Три", 4: "Четыре"}
            for line in file:
                dig = line.split()
                dig_val = int(dig[2])
                dig_name = rus_dig[dig_val]
                dig[0] = dig_name
                new_line = " ".join(dig)
                file_result.write(f'{new_line}\n')
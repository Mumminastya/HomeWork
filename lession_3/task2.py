def pers_info(name, surname, birth_year, city, e_mail, tel="Нет телефона"):
    return f'{name}, {surname}, {birth_year}, {city}, {e_mail}, {tel}'


def task_2():
    name = input("Имя: ")
    surname = input("Фамилия: ")
    birth_year = input("Год рождения: ")
    city = input("Город проживания: ")
    e_mail = input("e-mail: ")
    tel = input("Телефон: ")
    result = pers_info(name=name, surname= surname, birth_year=birth_year, city=city, e_mail=e_mail, tel=tel)
    print(result)

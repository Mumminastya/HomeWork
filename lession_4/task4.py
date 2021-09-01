def task_4():

    init_list = [111, 5, 8, 222, 16, 333, 8, 444, 5, 8, 555, 666, 89, 5, 89, 777, 888, 16, 16, 999]
    res_list = [i for i in init_list if init_list.count(i) == 1]
    print(res_list)

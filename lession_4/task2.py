def task_2():

    init_list = [300, 2, 12, 44, 1, 56]
    res_list = [init_list[i] for i in range(len(init_list)) if (i > 0 and init_list[i] > init_list[i - 1])]
    print(res_list)

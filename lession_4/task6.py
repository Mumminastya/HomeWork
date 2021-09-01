def task_6():
    from itertools import count, cycle

    start = int(input("Start: "))
    finish = int(input("Finish: "))
    for el in count(start):
        if el > finish:
            break
        else:
            print(el)

    iter_count = int(input("element count: "))
    i = 0
    for el in cycle([1, 2, 3, 4, 5]):
        if i > iter_count:
            break
        print(el)
        i += 1

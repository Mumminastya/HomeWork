def task_7():
    def fact(n):
        i = 1
        for j in range(1, n + 1):
            i = i * j
            yield i

    for p in fact(10):
        print(p)

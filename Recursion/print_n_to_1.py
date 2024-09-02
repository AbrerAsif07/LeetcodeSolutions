# constraint: without using -
def func(i, n):
    if i < n:
        return
    func(i, n + 1)
    print(n)


func(5, 1)


def func(i, n):
    if i > n:
        return
    func(i + 1, n)
    print(i)


func(1, 4)

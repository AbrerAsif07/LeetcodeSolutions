# constraint: without using -
def func(i, n):
    if i < n:
        return
    func(i, n + 1)
    print(n)


func(5, 1)
def func(i, n):
    if i < n:
        return
    print(i)
    func(i - 1, n)


func(5, 1)

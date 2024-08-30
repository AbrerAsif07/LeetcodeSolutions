# def greet():
#     print("hello world")
#     greet()


# greet()


def func(i, n):
    if i > n:
        return
    print("Asif")
    func(i + 1, n)


func(1, 3)


def func(i, n):
    if i < n:
        return
    print(i)
    func(i - 1, n)


func(5, 1)

def fib(index):
    if index == 0:
        return index
    elif index == 1:
        return index
    return fib(index - 1) + fib(index - 2)


x = fib(6)
print(x)

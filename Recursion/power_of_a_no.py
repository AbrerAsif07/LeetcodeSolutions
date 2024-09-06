def pow(n, p):
    result = 1
    if n == 1:
        return 1
    for i in range(p):
        result = result * n

    return result


x = pow(2, 4)
print(x)

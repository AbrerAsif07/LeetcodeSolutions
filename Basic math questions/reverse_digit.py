def reverse(x: int) -> int:
    n = x
    result = 0
    while n > 0:
        ld = n % 10
        result = (result * 10) + ld
        n = n // 10
    return result


print(reverse(123))

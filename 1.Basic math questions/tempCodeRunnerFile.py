def revint(x: int) -> int:
    rev_int = 0
    if -9 <= x <= 9:
        return x

    is_negative = x < 0
    x = abs(x)

    while x > 0:
        ld = x % 10
        x = x // 10
        rev_int = (rev_int * 10) + ld

    if is_negative:
        rev_int = -rev_int

    return rev_int


print(revint(123))
print(revint(-123))

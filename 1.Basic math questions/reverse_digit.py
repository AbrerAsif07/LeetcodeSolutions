def reverse(x: int) -> int:
    n = x
    result = 0
    while n > 0:
        ld = n % 10
        result = (result * 10) + ld
        n = n // 10
    return result


print(reverse(1))


# TC= O(log10N)
# SC= O(1)
def revint(n):
    rever_num = 0
    if -9 <= n <= 9:  # returning all single digit as they are
        return n
    # Handle negative numbers by keeping track of the sign
    is_negative = n < 0
    n = abs(n)  # Work with absolute value for simplicity
    x = n  # we do want to changer actual value of n, since we will modify it so dummy var
    while x > 0:
        last_digit = x % 10  # extract last digit
        x = x // 10  # remove last digit from n
        rever_num = (rever_num * 10) + last_digit

    # Reapply the negative sign if the original number was negative
    if is_negative:
        rever_num = -rever_num

    return rever_num


print(revint(123))

def check_palindrome(num: int) -> bool:
    result = 0
    n = num
    while n > 0:
        ld = n % 10
        result = (result * 10) + ld
        n = n // 10
    return result == num


print(check_palindrome(1))


# TC = O(log10N)
# SC = O(1)

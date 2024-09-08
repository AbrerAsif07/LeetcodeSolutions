import math


def checkPalindrome(num: int) -> bool:
    nod = math.floor(math.log10(num) + 1)
    result = 0
    n = num
    while n > 0:
        ld = n % 10
        result = result + (ld**nod)
        n = n // 10
    return result == num


print(checkPalindrome(370))

# TC=O(log10N)
# SC=O(1)

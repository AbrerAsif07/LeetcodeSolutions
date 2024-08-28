# TC= O(1)
# SC=O(1)

import math


def count_dig(num):
    return math.floor(math.log10(num) + 1)


print(count_dig(1234))

import math


def count_digits(num: int) -> int:
    return math.floor(math.log10(num) + 1)


print(count_digits(1234))

# You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.
# You should return the array of nums such that the the array follows the given conditions:
# 1.Every consecutive pair of integers have opposite signs.
# 2.For all integers with the same sign, the order in which they were present in nums is preserved.
# 3.The rearranged array begins with a positive integer.


def reArrange(nums):
    n = len(nums)
    result = [0] * n
    l = 0
    r = 1
    for i in range(0, n):
        if nums[i] > 0:
            result[l] = nums[i]
            l += 2
        else:
            result[r] = nums[i]
            r += 2

    return result


nums = [3, 1, -2, -5, 2, -4]
x = reArrange(nums)
print(x)

# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array


def majElement(nums):
    candidate = nums[0]
    count = 1
    n = len(nums)
    for i in range(1, n):
        if nums[i] == candidate:
            count += 1
        else:
            count -= 1

        if count == 0:
            candidate = nums[i]
            count = 1
    return candidate


nums = [5, 5, 2, 1, 1, 5, 5, 7, 5, 5, 8, 5, 5, 5, 5]
x = majElement(nums)
print(x)

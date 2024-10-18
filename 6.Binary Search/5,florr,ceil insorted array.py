# nums = [1, 3, 5, 6]
# target = 4
# floor=3,ceil=5


def findFLoorCeil(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    floor = -1
    ceil = -1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return target, target

        elif nums[mid] < target:
            floor = nums[mid]
            low = mid + 1

        else:
            ceil = nums[mid]
            high = mid - 1

    return [floor, ceil]


nums = [1, 3, 5, 6]
target = 4
x = findFLoorCeil(nums, target)
print(x)

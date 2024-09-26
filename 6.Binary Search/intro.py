nums = [2, 4, 6, 7, 10, 11, 16, 18]


def BinarySearch(nums, target):
    n = len(nums)
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid

        elif target < nums[mid]:
            high = mid - 1

        else:
            low = mid + 1

    return -1


target = 6
nums = [2, 4, 6, 7, 10, 11, 16, 18]
x = BinarySearch(nums, target)
print(x)


nums = [2, 4, 6, 7, 10, 11, 16, 18]

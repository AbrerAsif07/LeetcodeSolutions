nums = [1, 3, 5, 6]


def searchPosi(nums, target):
    n = len(nums)
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid

        elif target < nums[mid]:
            high = mid - 1
            return mid + 1

        else:
            low = mid + 1

    return low


nums = [1, 3, 5, 6]
target = 2
x = searchPosi(nums, target)
print(x)

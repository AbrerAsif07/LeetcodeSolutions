def findFloor(nums, n, x):
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == x:
            return mid

        elif x > nums[mid]:
            low = mid + 1

        else:
            high = mid - 1

    return high


nums = [1, 2, 8, 10, 11, 12, 19]
n = 7
x = 13
z = findFloor(nums, n, x)
print(z)

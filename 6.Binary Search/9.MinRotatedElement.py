def findMin(nums):
    low = 0
    high = len(nums) - 1
    minimum = float("inf")

    while low <= high:
        mid = (low + high) // 2

        if nums[low] <= nums[mid]: #if it is smaller it indicates that sub arr is sorted, so min will lie on other side
            minimum = min(minimum, nums[low])
            low = mid + 1

        else:
            minimum = min(minimum, nums[mid])
            high = mid - 1

    return minimum


nums = [4, 5, 6, 7, 0, 1, 2]
x = findMin(nums)
print(x)

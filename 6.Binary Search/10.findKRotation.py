# Input: arr = [5, 1, 2, 3, 4]
def findKRotation(nums):
    l = 0
    h = len(nums) - 1
    while l <= h:
        mid = (l + h) // 2
        if nums[mid] < nums[mid - 1]:
            return mid
        if nums[mid] > nums[mid + 1]:
            return mid + 1

        if nums[mid] < nums[h]:
            h = mid - 1

        else:
            l = mid + 1
    return 0


nums = [5, 1, 2, 3, 4]
x = findKRotation(nums)
print(x)

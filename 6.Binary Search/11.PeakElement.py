# nums=[5,10,20,15]
def peakElement(nums):  # return type is index
    l = 0
    h = len(nums) - 1
    while l < h:
        mid = (l + h) // 2
        if nums[mid] < nums[mid + 1]:
            l = mid + 1
        else:
            h = mid

    return l


nums = [5, 4, 3, 2, 1]
x = peakElement(nums)
print(x)

a = 5
print(type(a))

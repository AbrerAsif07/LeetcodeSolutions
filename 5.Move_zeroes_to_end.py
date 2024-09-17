def moveZeroes(nums):
    i = 0
    j = i + 1
    n = len(nums)
    for j in range(n):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    return nums


nums = [0, 1, 0, 3, 12]
x = moveZeroes(nums)
print(x)

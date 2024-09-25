def NextPermutation(nums):
    n = len(nums)
    index = -1
    for i in range(n - 2, -1, -1):
        if nums[i - 1] < nums[i]:
            nums[i - 1] = index
            break

        if index == -1:
            nums.reverse()
            return

    for i in range(n - 1, index, -1):
        if nums[i] > nums[index]:
            nums[i], nums[index] = nums[index], nums[i]
            break

        nums[:] = nums[0 : index + 1] + reversed(nums[index + 1 :])
    return nums


nums = [2, 3, 5, 4, 1, 0, 0]
x = NextPermutation(nums)
print(x)

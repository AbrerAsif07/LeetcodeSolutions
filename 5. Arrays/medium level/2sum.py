def twoSum(nums, target):
    n = len(nums)
    hash_map = {}
    for i in range(0, n):
        remaining = target - nums[i]
        if remaining in hash_map:
            return [hash_map[remaining], i]
        hash_map[nums[i]] = i


nums = [2, 3, 5, 11, 6, 8]
x = twoSum(nums, 14)
print(x)

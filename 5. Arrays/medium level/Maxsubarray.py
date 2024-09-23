# Input: nums = [5, 4, -1, 7, 8]
# Output: 23


def maxSubarray(nums):
    n = len(nums)
    current_sm = 0
    for i in range(0, n):
        max_no = nums[i]
        current_sm += max_no
        max_no = max(max_no, current_sm)
        if max_no < 0:
            current_sm = 0

    return max_no


nums = [2, 3, -8, 7, -1, 2, 3]
x = maxSubarray(nums)
print(x)

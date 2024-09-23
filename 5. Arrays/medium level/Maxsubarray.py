# Input: nums = [5, 4, -1, 7, 8]
# Output: 23


def maxSubarray(nums):
    n = len(nums)
    current_sm = 0
    max_no = float("-inf")
    for i in range(0, n):
        max_no = nums[i]
        current_sm += nums[i]
        max_no = max(max_no, current_sm)
        if current_sm < 0:
            current_sm = 0

    return max_no


nums = [5, 7, 8, 9, -10, 5, 4, 3, 2, -100, 5, 7, 8, 100]

x = maxSubarray(nums)
print(x)
# TC=O(N)
# SC=O(1)

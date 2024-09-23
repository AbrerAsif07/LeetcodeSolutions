# Input: prices = [7, 1, 5, 3, 6, 4]
# Output: 5


def maxBuySell(nums):
    l = 0
    max_profit = 0
    for i in range(0, len(nums) - 1):
        if nums[i + 1] < nums[i]:
            l = nums[i + 1]  # Assign nums[i + 1] to l

        for i in range(l, len(nums)):

            profit = nums[i] - l
            max_profit = max(max_profit, profit)

        return max_profit


nums = [7, 6, 4, 3, 1]
x = maxBuySell(nums)
print(x)

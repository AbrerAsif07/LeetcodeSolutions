# nums = [100, 4, 200, 1, 3, 2]


# def LongestConsecutive(nums):
#     if not nums:  # Check if the input list is empty
#         return 0
#     result = []
#     nums.sort()
#     for i in range(0, len(nums) - 1):
#         if nums[i + 1] == nums[i] + 1:
#             result.append(nums[i + 1])

#     return len(result) + 1


# nums = [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]
# x = LongestConsecutive(nums)
# print(x)


class Solution:
    def longestConsecutive(self, nums):
        if not nums:  # Check if the input list is empty
            return 0

        nums = set(nums)  # Convert to set to handle duplicates and allow O(1) lookups
        longest_streak = 0

        for num in nums:
            # Only check for the start of a sequence (if num-1 is not in the set)
            if num - 1 not in nums:
                current_num = num
                current_streak = 1

                # Check for consecutive elements in the sequence
                while current_num + 1 in nums:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak


# Example usage:
nums = [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]
x = Solution().longestConsecutive(nums)
print(x)


# Optimal
class Solution:
    def longestConsecutive(self, nums):
        my_set = set()
        for num in nums:
            my_set.add(num)  # Add all elements in set
        longest = 0  # KEEPS COUNT OF LONGEST CONSECUTIVE
        for num in my_set:
            if (
                num - 1 not in my_set
            ):  # Just smaller element not present go to next element in set
                x = num
                count = 1
                while x + 1 in my_set:
                    count += 1  # keeps track of sequence length
                    x += 1  # keeps on traversing to next greater
                longest = max(longest, count)
        return longest


nums = [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]
x = Solution().longestConsecutive(nums)
print(x)

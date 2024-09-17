from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        n = len(nums)
        k = k % n  # Handle cases where k > n

        reverse(n - k, n - 1)
        reverse(0, n - k - 1)
        reverse(0, n - 1)


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
solution = Solution()
solution.rotate(nums, k)  # Rotates the array in-place
print(f"Rotated array: {nums}")

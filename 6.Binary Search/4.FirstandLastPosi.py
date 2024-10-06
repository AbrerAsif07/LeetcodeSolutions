def searchRange(nums, target):
    # Helper function to find the first or last occurrence of the target
    def binarySearch(nums, target, findFirst):
        left, right = 0, len(nums) - 1
        occurrence = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                occurrence = mid
                if findFirst:
                    right = (
                        mid - 1
                    )  # Continue searching left side to find the first occurrence
                else:
                    left = (
                        mid + 1
                    )  # Continue searching right side to find the last occurrence
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return occurrence

    # Find first occurrence of target
    first_occurrence = binarySearch(nums, target, findFirst=True)

    # If target is not found, return [-1, -1]
    if first_occurrence == -1:
        return [-1, -1]

    # Find last occurrence of target
    last_occurrence = binarySearch(nums, target, findFirst=False)

    return [first_occurrence, last_occurrence]


# Test cases
nums = [5, 7, 7, 8, 8, 10]
target = 8
print(searchRange(nums, target))  # Output: [3, 4]

nums = [5, 7, 7, 8, 8, 10]
target = 6
print(searchRange(nums, target))  # Output: [-1, -1]

nums = []
target = 0
print(searchRange(nums, target))  # Output: [-1, -1]
print("hello world")
print("imma hoe")

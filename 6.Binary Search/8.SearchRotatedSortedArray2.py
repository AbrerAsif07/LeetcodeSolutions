def search(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return True

        if (
            nums[mid] == nums[high] == nums[low]
        ):  # When all three pointers (low, mid, high) point to the same value,
            # we can’t determine whether the left or right half is sorted.
            low = low + 1
            high = high - 1

        elif nums[low] <= nums[mid]:
            if nums[low] <= target < nums[mid]:
                high = mid - 1

            else:
                low = mid + 1

        else:
            if nums[mid] < target <= nums[high]:
                low = mid + 1

            else:
                high = mid - 1

    return False


nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 13, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
target = 13
x = search(nums, target)
print(x)

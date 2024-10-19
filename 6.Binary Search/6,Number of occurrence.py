def Occurence(nums, target):
    count = 0

    def findFirstOccurence(nums, target):
        low = 0
        high = len(nums) - 1
        first_occurence = -1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                first_occurence = mid
                high = mid - 1  # searches to the right to find first occurence
            elif nums[mid] > target:
                high = mid - 1

            else:
                low = mid + 1
        return first_occurence

    def findLastOccurence(nums, target):
        low = 0
        high = len(nums) - 1
        last_occurrence = -1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                last_occurrence = mid
                low = mid + 1

            elif nums[mid] > target:
                high = mid - 1

            else:
                low = mid + 1

        return last_occurrence

    first = findFirstOccurence(nums, target)
    last = findLastOccurence(nums, target)

    count = last - first + 1

    return count


nums = [1, 1, 2, 2, 2, 2, 3]
target = 2

x = Occurence(nums, target)
print(x)

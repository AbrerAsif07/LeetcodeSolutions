# Higher Bound deals with the element just greater than the target value provided


def find_floor_and_ceiling(arr, x):
    floor = -1
    ceiling = -1

    for num in arr:
        # Update Floor
        if num <= x and (floor == -1 or num > floor):
            floor = num

        # Update Ceiling
        if num >= x and (ceiling == -1 or num < ceiling):
            ceiling = num

    return [floor, ceiling]


# Example usage
arr = [5, 6, 8, 9, 6, 5, 5, 6]
x = 7
result = find_floor_and_ceiling(arr, x)
print(result)  # Output: [6, 8]


# Input: x = 7 , nums = [5, 6, 8, 9, 6, 5, 5, 6]
# Output: 6, 8


def getFloorAndCeil(nums, x):
    floor = -1
    ceil = -1
    for num in nums:
        if num <= x:
            if floor == -1 or num > floor:
                floor = num

        if num >= x:
            if ceil == -1 or num < ceil:
                ceil = num
    return floor, ceil


x = 7
nums = [3, 4, 5, 6, 8, 9, 6, 5, 5, 6, 10]
y = getFloorAndCeil(nums, x)
print(y)

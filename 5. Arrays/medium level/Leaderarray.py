# nums=[16,17,4,3,5,2]
def leaderArr(nums, n):
    maxi = float("-inf")
    result = []
    for i in range(n - 1, -1, -1):
        if nums[i] > maxi:
            maxi = nums[i]
            result.append(maxi)

    return list(reversed(result))


nums = [16, 17, 4, 3, 5, 2]
n = len(nums)
x = leaderArr(nums, n)
print(x)


def leaderArr(nums, n):
    maxi = float("-inf")  # Initialize maxi to negative infinity
    result = []

    for i in range(n - 1, -1, -1):
        if nums[i] > maxi:  # Only add if the current element is strictly greater
            maxi = nums[i]
            result.append(maxi)

    return list(reversed(result))  # Return the reversed list


nums = [16, 17, 4, 3, 5, 2]
n = len(nums)  # Define n as the length of the array
x = leaderArr(nums, n)
print(x)

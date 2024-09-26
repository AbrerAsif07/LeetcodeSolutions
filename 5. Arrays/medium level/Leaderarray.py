# nums=[16,17,4,3,5,2]
def leaderArr(nums, n):
    maxi = float("-inf")
    result = []
    for i in range(n - 1, -1, -1):
        if nums[i] > maxi:
            maxi = nums[i]
            result.append(maxi)

    return list(reversed(result))



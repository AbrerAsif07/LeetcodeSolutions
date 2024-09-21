# Given an array arr containing n integers and an integer k. 
# Your task is to find the length of the longest Sub-Array with the sum of the elements equal to the given value k.

def LargestSubarray(arr, k):
    n = len(arr)
    sum_map = {}
    sum = 0
    max_length = 0
    for i in range(0, n):
        sum += arr[i]
        if sum == k:
            max_length += 1

        rem = sum - k
        if rem in sum_map:
            L = i - sum_map[rem]
            max_length = max(max_length, L)

        if sum not in sum_map:
            sum_map[sum] = i

    return max_length


arr = [1, 2, 3, 1, 1, 1, 1, 3, 3]
x = LargestSubarray(arr, 3)
print(x)


# TC=O(N)
# SC=O(1)
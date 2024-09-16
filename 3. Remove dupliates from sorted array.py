# Brute force
# def RemoveDuplicates(arr):
#     n = len(arr)
#     dic = {}
#     for i in range(0, n):
#         dic[arr[i]] = 0

#     j = 0
#     for key in dic:
#         arr[j] = key
#         j += 1
#     return len(dic), arr


# arr = [0, 0, 1, 1, 1, 2, 4, 4, 4, 5, 5, 6, 6, 6, 6]
# unique_elements, sorted_array = RemoveDuplicates(arr)
# print(f"unique elements= {unique_elements}")
# print(f"sorted array= {sorted_array}")

# TC=O(2N)
# SC=0(K)

# Optimised Solution


def RemoveDuplicates(arr):
    n = len(arr)
    i = 0
    j = i + 1
    if n == 1:
        return 1
    while j < n:
        if arr[j] != arr[i]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        j += 1

    return i + 1, arr


arr = [0, 0, 1, 1, 1, 2, 4, 4, 4, 5, 5, 6, 6, 6, 6]
unique_elements, sorted_array = RemoveDuplicates(arr)
print(f"unique elements= {unique_elements}")
print(f"sorted array= {sorted_array}")

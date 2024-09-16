def RemoveDuplicates(arr):
    n = len(arr)
    dic = {}
    for i in range(0, n):
        dic[arr[i]] = 0

    j = 0
    for key in dic:
        arr[j] = key
        j += 1
    return len(dic), arr


arr = [0, 0, 1, 1, 1, 2, 4, 4, 4, 5, 5, 6, 6, 6, 6]
unique_elements, sorted_array = RemoveDuplicates(arr)
print(f"unique elements= {unique_elements}")
print(f"sorted array= {sorted_array}")

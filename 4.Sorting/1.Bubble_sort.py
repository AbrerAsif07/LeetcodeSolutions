def Bubblesort(arr):
    n = len(arr)
    for i in range(n - 2, -1, -1):
        for j in range(0, i + 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
Bubblesort(arr)
print(arr)



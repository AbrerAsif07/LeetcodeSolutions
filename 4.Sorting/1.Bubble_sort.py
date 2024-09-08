def Bubblesort(arr):
    n = len(arr)
    for i in range(n - 2, -1, -1):
        for j in range(0, i + 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
Bubblesort(arr)
print(arr)


def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements in reverse order
    for i in range(n - 2, -1, -1):
        # Last i elements are already in place
        for j in range(0, i + 1):
            # Traverse the array from 0 to i
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [64, 25, 12, 22, 11]
bubble_sort(arr)
print(arr)

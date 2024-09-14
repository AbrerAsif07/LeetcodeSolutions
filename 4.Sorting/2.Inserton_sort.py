# Insertion sort  is a sorting algorithm that uses i,j and key


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key


arr = [3, 5, 6, 86, 28, 7, 12]
insertion_sort(arr)
print(arr)

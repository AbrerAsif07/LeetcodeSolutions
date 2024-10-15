# Better Solution
def secondarr(arr):
    maxi = float("-inf")
    second_maxi = float("-inf")
    mini = float("inf")
    second_mini = float("inf")
    n = len(arr)
    for i in range(0, n):
        maxi = max(maxi, arr[i])
        mini = min(mini, arr[i])

    for i in range(0, n):
        if arr[i] > second_maxi and arr[i] != maxi:
            second_maxi = arr[i]

        if arr[i] < second_mini and arr[i] != mini:
            second_mini = arr[i]

    return second_maxi, second_mini


arr = [5, -10, 13, 67, 89, -100, 55]
second_largest, second_smallest = secondarr(arr)

# Output the results
print("Second largest:", second_largest)
print("Second smallest:", second_smallest)


# TC = O(2N) ALMOST EQUALS TO O(N)
# SC=O(1)


def secondLargest(arr):
    n = len(arr)
    maxi = float("-inf")
    second_maxi = float("-inf")
    mini = float("inf")
    second_mini = float("inf")

    for i in range(0, n):
        if arr[i] > maxi:
            second_maxi = maxi
            maxi = arr[i]

        elif arr[i] > second_maxi and arr[i] != maxi:
            second_maxi = arr[i]

        if arr[i] < mini:
            second_mini = mini
            mini = arr[i]

        elif arr[i] < second_mini and arr[i] != mini:
            second_mini = arr[i]

    return second_maxi, second_mini


arr = [5, 10, 13, 67, 89, -100, 55, 78]
second_largest, second_smallest = secondLargest(arr)
print(f"Second largest element = {second_largest}")
print(f"Second smallest element = {second_smallest}")
print("hello world")

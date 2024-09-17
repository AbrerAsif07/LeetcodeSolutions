def searchInSorted(self, arr, N, K):
    N = len(arr)
    for i in range(0, N):
        if arr[i] == K:
            return 1
    return -1


print("hello world")

# TC=O(N)
# SC=O(1)

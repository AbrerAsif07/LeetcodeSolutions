def sortRotate(arr):
    n = len(arr)
    rotations = 0
    for i in range(0, n):
        if arr[i] > arr[(i + 1) % n]:
            rotations += 1
        if rotations > 1:
            return False
    return True


arr = [5, 8, 9, 11, 6, 13, 14, 15]
x = sortRotate(arr)
print(x)

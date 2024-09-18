def findMaxConsecutiveOnes(arr):
    count = 0  # Initialize count to zero
    count1 = 0  # Initialize count1 to zero

    # Traverse the array
    for i in range(len(arr)):
        if arr[i] == 1:
            count += 1  # Increment count if we encounter a '1'
        else:
            count = 0  # Reset count to zero if it's not '1'

        count1 = max(count, count1)  # Update count1 with the maximum value

    return count1  # Return the maximum number of consecutive 1s


# Example usage
array = [1, 1, 0, 1, 1, 1]
print(findMaxConsecutiveOnes(array))  # Output: 3

def NextPermutation(nums):
    n = len(nums)
    index = -1
    for i in range(n - 2, -1, -1): #Comparison starts with right 0 to left 0, then 1 and 0
        if nums[i ] < nums[i+1]:
            index=i #Labelling the breakpoint
            break

    if index == -1:    #If no breakpoint found then reverse the entire array 
            nums.reverse() 
            return nums

    for i in range(n - 1, index, -1): #Finalyy swap breakpoint value with no just greater than brealpoint here 3
        if nums[i] > nums[index]:
            nums[i], nums[index] = nums[index], nums[i]
            break

    nums[index+1:]=reversed(nums[index+1:]) #all portion to the right of break point is reversed
    


nums = [2, 3, 5, 4, 1, 0, 0]
x = NextPermutation(nums)
print(x)

# TC=O(3N)
# SC=O(1)
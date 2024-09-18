def singleno(nums):
    dic = {}
    for i in range(len(nums)):
        num = nums[i]
        current_count = dic.get(num, 0)
        dic[num] = current_count + 1

    for num in dic:
        if dic[num] == 1:
            return num


nums = [4, 1, 2, 1, 2]
print(singleno(nums))

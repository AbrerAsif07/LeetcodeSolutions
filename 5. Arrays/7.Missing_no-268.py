def missNo(nums):
    n = len(nums)
    ori_arr_total = (n * (n + 1)) // 2
    return ori_arr_total - sum(nums)


nums = [3, 0, 1]
missing_no = missNo(nums)
print(f"missing no is = {missing_no}")

# TC = O(N)
# SC=O(1)

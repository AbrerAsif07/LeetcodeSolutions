# def pow(n, p):
#     result = 1
#     if n == 1:
#         return 1
#     for i in range(p):
#         result = (
#             result * n
#         )  # here s runs from 0 to p-1 times and result iterates to p tiumes multiplying itslef with updated value

#     return result


# x = pow(2, 4)
# print(x)


# Optimised solution


def pow(b, p):
    if p == 0:
        return 1
    if p == 1:
        return b
    return b * pow(b, p - 1)


x = pow(2, 4)
print(x)

# SC = O(POWER)
# TC= O(POWER)  As it runs for the no of power 
# reversing using 2 pointers and 1 pointer with same tc and sc


def rev(lst, start, end):
    if start > end:
        return
    lst[start], lst[end] = lst[end], lst[start]
    rev(lst, start + 1, end - 1)


l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
rev(l, 0, len(l) - 1)
print(l)  # since it has made changes to the list itslef so print list

# Alternative method: Using a single pointer ie index


def revarr(lst, index):
    l = len(lst)
    if index == l // 2:
        return
    lst[index], lst[l - 1 - index] = lst[l - 1 - index], lst[index]
    revarr(lst, index + 1)


l1 = [10, 79, 3, 4, 5, 69]
revarr(l1, 0)
print(l1)

# Hashing deals with the logic of prestoring frequency and then fetching
lst = [5, 4, 2, 5, 4, 2, 1, 1, 1, 3, 5, 3]

dic = {}

for num in lst:
    dic[num] = dic.get(num, 0) + 1
print(dic)

x = int(input("Enter no whose repition value you want to see = "))
print(dic.get(x, 0))


lst1 = [5, 2, 1]
for num in lst1:
    print(dic.get(num, 0))

# T.C.= O(n+m) where n= len of lst and m= len of lst1
# S.C.= O(n)

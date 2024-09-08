string = "aerrropllane"
l1 = [0] * 26

for ch in string:
    i = ord(ch) - 97
    l1[i] += 1
print(l1)

x = input("Enter char whose count you want to display = ")
print(l1[ord(ch) - 97])

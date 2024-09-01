# constraint: without using +
def func(i, n):
    if i < n:
        return
    func(i - 1, n)
    print(i)


func(5, 1)
# Backtracking used to subsequently run function 5 times and print i ie 5,4,3,2,1 in reverse order

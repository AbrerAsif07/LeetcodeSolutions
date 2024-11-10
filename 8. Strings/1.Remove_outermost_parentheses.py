def remPar(s: str) -> str:
    count = 0
    result = ""  # No extra space initially, all empty
    for char in s:  # a while loop doesnt understand s
        if char == "(":
            count += 1
            if count > 1:
                result = result + "("  # cannot use append as it is used for lists

        elif char == ")":
            count -= 1
            if count > 0:
                result = result + ")"

    return result


print(remPar("()()"))

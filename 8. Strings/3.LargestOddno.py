def largestOddNumber(num: str) -> str:
    for i in range(
        len(num) - 1, -1, -1
    ):  # backward traversing to find largest odd substring
        if (
            int(num[i]) % 2 != 0
        ):  # converting string to int for individual int, to check if encountered odd
            return num[
                : i + 1
            ]  # if odd encountered then returned from begin to upto that odd no
    return ""


print(largestOddNumber("572"))

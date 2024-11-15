# Input: s = "paperpe", t = "titlesl"

# Output: true


def isIsomorphic(s: str, t: str) -> bool:
    mapping_s_to_t = {}
    mapping_t_to_s = {}  # for edge case, badc and baba

    for i in range(len(s)):  # both length should be same to be isomorphic
        char_s = s[i]  # assigning variable
        char_t = t[i]

        if char_s in mapping_s_to_t:  # checking if char of s exists in mapping s to t
            if mapping_s_to_t[char_s] != char_t:  # if char s already not unique
                return False

        else:
            mapping_s_to_t[char_s] = (
                char_t  # if not inserted yet then char of s  inserted as key value pair with char of t
            )

        # edge case eg, "badc" and"baba"
        if char_t in mapping_t_to_s:  # checking if char of t exists in mapping t to s
            if mapping_t_to_s[char_t] != char_s:  # if char s already not unique
                return False

        else:
            mapping_t_to_s[char_t] = (
                char_s  # if not inserted yet then char of s  inserted as key value pair with char of t
            )

    return True


print(isIsomorphic(s="paperpe", t="titlesl"))

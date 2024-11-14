# Input: strs = ["flower","flow","flight"]
# Output: "fl"
from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    if len(strs) == 0:  # if empty list
        return ""

    base = strs[0]
    for i in range(len(base)):  # this will loop entire base string thro index
        for word in strs[1:]:  # this will loop remaining words/strings
            if (
                i == len(word) or word[i] != base[i]
            ):  # first check if remaining word exhausted, second check mismatch words with base string
                return base[0:i]  # since slicing excludes ith index

    return base  # edge case if first word is shortest


print(longestCommonPrefix(strs=["flower", "flow", "flight"]))

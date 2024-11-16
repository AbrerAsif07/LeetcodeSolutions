# An anagram is a word, phrase, or sequence of characters formed by rearranging the letters of another word or phrase, using all the original letters exactly once.
# Key Points of an Anagram:
# The number of characters and their frequencies must match in both words.
# The order of letters can be rearranged, but the composition of letters remains identical.
# readme: Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:

# Input: s = "rat", t = "car"
# Output: false


def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    return sorted(s) == sorted(t)


print(isAnagram(s="anagram", t="nagaram"))
print(isAnagram(s="rat", t="car"))

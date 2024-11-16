# Input: s = "abcde", goal = "cdeab"
# Output: true


def rotateString(s: str, goal: str) -> bool:
    if len(s) != len(goal):
        return False
    double_s = s + s
    if goal in double_s:
        return True
    else:
        return False


print(rotateString(s="abcde", goal="abced"))
# Tc=O(n)
# sc=O(N)

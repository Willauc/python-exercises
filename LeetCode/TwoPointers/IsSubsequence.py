# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
#
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none)
# of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a
# subsequence of "abcde" while "aec" is not).

def isSubsequence(s: str, t: str) -> bool:
    SIndex = 0

    if len(s) == 0:
        return True
    elif len(s) == len(t):
        return s == t

    for char in t:
        if char == s[SIndex]:
            SIndex += 1
        if SIndex == len(s):
            return True

    return False


if __name__ == '__main__':
    s = "abc"
    t = "ahbgdc"
    print(isSubsequence(s, t))

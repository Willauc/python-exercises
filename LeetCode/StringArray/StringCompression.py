# Given an array of characters chars, compress it using the following algorithm:
#
# Begin with an empty string s. For each group of consecutive repeating characters in chars:
#
# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead, be stored in the input character array chars.
# Note that group lengths that are 10 or longer will be split into multiple characters in chars.
#
# After you are done modifying the input array, return the new length of the array.
#
# You must write an algorithm that uses only constant extra space.
from typing import List

def compress(chars: List[str]) -> int:
    chars_len = len(chars)
    if chars_len == 0: return 0

    s = []
    ptr1 = 0
    ptr2 = 1
    compteur = 1

    while ptr1 < len(chars):
        char_courant = chars[ptr1]


        while ptr2 < chars_len and char_courant == chars[ptr2]:
            compteur += 1
            ptr2 += 1

        s.append(char_courant)
        if compteur > 1 :
            for n in list(str(compteur)):
                s.append(n)
        ptr2 += 1
        ptr1 = ptr2 - 1
        compteur = 1

    chars[:] = s
    print(chars)
    return len(s)


if __name__ == "__main__":
    chars = ["a", "a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a", "c", "c", "e", "f"]
    print(compress(chars))

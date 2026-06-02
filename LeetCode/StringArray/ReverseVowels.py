# Given a string s, reverse only all the vowels in the string and return it.
#
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.


def reverseVowels(s: str) -> str:
    liste1 = list(s)
    liste2 = []
    liste_vowels = set("aAeEiIoOuU")

    for car in liste1:
        if car in liste_vowels:
            liste2.append(car)
    for i in range(len(liste1)):
        if liste1[i] in liste_vowels:
            liste1[i] = liste2.pop()

    return "".join(liste1)


# Version with 2 pointer O(n)
def reverseVowelsTwoPointer(self, s: str) -> str:
    vowels = set("aeiouAEIOU")
    s = list(s)

    left, right = 0, len(s) - 1

    while left < right:
        while left < right and s[left] not in vowels:
            left += 1
        while left < right and s[right] not in vowels:
            right -= 1

        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    return "".join(s)


if __name__ == "__main__":
    print("Test 1: ")
    print(reverseVowels("IceCreAm") == "AceCreIm")
    print("Test 2: ")
    print(reverseVowels("leetcode") == "leotcede")

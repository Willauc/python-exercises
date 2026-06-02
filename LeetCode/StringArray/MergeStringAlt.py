#You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
#
#Return the merged string.

def mergeAlternately(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: str
    """
    word1, word2 = word1.lower().replace(" ", ""), word2.lower().replace(" ", "")

    final_word = ""

    while word1 != "" and word2 != "":
        final_word += word1[0]
        final_word += word2[0]

        word1 = word1[1:]
        word2 = word2[1:]

        if word1 == "" and word2 != "":
            final_word += word2
            word2 = ""
        elif word1 != "" and word2 == "":
            final_word += word1
            word1 = ""
    return final_word


# Autre solution trouver sur leetcode.
def mergeAlternatelySolution(word1, word2):
    result = []
    i = 0
    while i < len(word1) or i < len(word2):
        if i < len(word1):
            result.append(word1[i])
        if i < len(word2):
            result.append(word2[i])
        i += 1
    return ''.join(result)


if __name__ == "__main__":
    result = mergeAlternately("abc", "def") == "adbecf"
    print("Test 1: " + str(result))

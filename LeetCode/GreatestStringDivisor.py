def gcdOfStrings(str1, str2):
    str3 = str2[:]
    while str3 != "":
        if str1 == str3 * (len(str1) // len(str3)) and len(str1) % len(str3) == 0 and str2 == str3 * (len(str2) // len(str3)) and len(str2) % len(str3) == 0:
            return str3
        else:
            str3 = str3[:-1]
    return ""

if __name__ == '__main__':
    result = gcdOfStrings("ABABAB", "ABAB") == "AB"
    print(gcdOfStrings("ABABAB", "ABAB"))
    print("test 1: " + str(result))
from typing import List


def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    result = []
    greatest_candies = max(candies)

    for kid in candies:
        if kid + extraCandies >= greatest_candies:
            result.append(True)
        else:
            result.append(False)

    return result




if __name__ == "__main__":
    result = kidsWithCandies([2,3,5,1,3], 3)
    print(result)
    print("Test 1: " + str(result == [True,True,True,False,True]))
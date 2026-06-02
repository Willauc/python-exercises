#You have a long flowerbed in which some of the plots are planted, and some are not.
#However, flowers cannot be planted in adjacent plots.
#
#Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty,
#and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers
#rule and false otherwise.
from typing import List


def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
    if n <= 0:
        return True

    count = 0
    for index in range(len(flowerbed)):
        next_index = index +1 if index < len(flowerbed) -1 else index
        past_index = index -1 if index != 0 else 0

        if flowerbed[index] == 0 and flowerbed[next_index] == 0 and (index == 0 or flowerbed[past_index] == 0):
            flowerbed[index] = 1
            count += 1
        if n <= count:
            return True

    return False



if __name__ == "__main__":
    result = canPlaceFlowers([1,0,0,0,1],1)
    print("Test 1: " + str(result))

    result = canPlaceFlowers([1, 0, 0, 0, 0, 1], 2)
    print("Test 2: " + str(result))
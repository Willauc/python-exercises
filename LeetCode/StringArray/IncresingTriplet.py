# Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and
# nums[i] < nums[j] < nums[k]. If no such indices exists, return false.
from typing import List


def increasingTriplet(nums: List[int]) -> bool:
    first = second = float('inf')

    for n in nums:
        if n <= first:
            first = n
        elif n <= second:
            second = n
        else:
            return True

    return False


if __name__ == "__main__":
    print("test 1 : ")
    print(increasingTriplet([1, 2, 3, 4, 5]) == True)

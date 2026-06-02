#Given an integer array nums, return an array answer such that answer[i] is equal to the product of all
# the elements of nums except nums[i].
#The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#
#You must write an algorithm that runs in O(n) time and without using the division operation.
from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:

    return []

if __name__ == "__main__":
    print(productExceptSelf([1,2,3,4]) == [24,12,8,6])
    print(productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0])
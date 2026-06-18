# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# Note that you must do this in-place without making a copy of the array.

from typing import List

def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    nums_len = len(nums)
    ptr1 = 0
    ptr2 = nums_len - 1

    while ptr1 < ptr2:
        if nums[ptr2] != 0:
            break
        elif ptr1 == ptr2 :
            return
        else :
            ptr2 -= 1

    while ptr1 < ptr2:
        while nums[ptr1] == 0 and ptr1 < ptr2:
            nums.append(nums.pop(ptr1))
            ptr2 -= 1
        ptr1 += 1






if __name__ == '__main__':
    nums_array = [0,1,0,3,2,1]
    moveZeroes(nums_array)
    print (nums_array)
# You are given an integer array nums and an integer k.
#
# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
#
# Return the maximum number of operations you can perform on the array.
from typing import List

def maxOperations(nums: List[int], k: int) -> int:
    ptr1 = 0
    ptr2 = len(nums) - 1
    count = 0
    while ptr2 > 0 :
        if k - nums[ptr1] == nums[ptr2]:
            nums.pop(ptr2)
            nums.pop(ptr1)
            count += 1
            ptr1 = 0
            ptr2 -= 2
        if ptr1 >= ptr2 :
            break

    return count

if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    k = 5
    print( maxOperations(nums, k) == 2)
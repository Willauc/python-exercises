# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of
# the ith line are (i, 0) and (i, height[i]).
#
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
#
# Return the maximum amount of water a container can store.
#
# Notice that you may not slant the container.

from typing import List

def maxArea(height: List[int]) -> int:
    pt1, pt2 = 0, len(height) - 1
    max_area = 0
    while pt1 < pt2:
        area = min(height[pt1], height[pt2]) * (pt2 - pt1)
        max_area = area if area > max_area else max_area

        if height[pt1] > height[pt2]:
            pt2 -= 1
        else :
            pt1 += 1

    return max_area


if __name__ == "__main__":
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(maxArea(height) == 49)

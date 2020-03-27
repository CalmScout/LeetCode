"""
Given an array nums, write a function to move all 0's to the end of it while maintaining
the relative order of the non-zero elements.

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        result = []
        for el in nums:
            if el:
                result.append(el)
        for i in range(len(result)):
            nums[i] = result[i]
        for i in range(len(result), len(nums)):
            nums[i] = 0

if __name__ == "__main__":
    inp = [0, 1, 0, 3, 12]
    out = [1, 3, 12, 0, 0]
    Solution().moveZeroes(inp)
    assert inp == out, (inp, out)

    inp = [0, 0, 1, 2, 3]
    out = [1, 2, 3, 0, 0]
    Solution().moveZeroes(inp)
    assert inp == out, (inp, out)

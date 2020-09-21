"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is
equal to the product of all the elements of nums except nums[i].

Constraint: It's guaranteed that the product of the elements of any prefix or suffix of
the array (including the whole array) fits in a 32 bit integer.
Note: Please solve it without division and in O(n).
Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
"""
from typing import List
import operator
from functools import reduce


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1 for _ in nums]
        
        left = 1
        right = 1
        
        for i in range(len(nums)):
            ans[i] *= left
            ans[-1-i] *= right
            left *= nums[i]
            right *= nums[-1-i]
        
        return ans


if __name__ == "__main__":
    inp = [1, 2, 3, 4]
    out = [24, 12, 8, 6]
    actual = Solution().productExceptSelf(inp)
    assert out == actual, (out, actual)

    # inp = [0, 0]
    # out = [0, 0]
    # actual = Solution().productExceptSelf(inp)
    # assert out == actual, (out, actual)

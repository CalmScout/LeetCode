"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
"""
from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total_sum = sum(range(len(nums) + 1))
        return total_sum - sum(nums)


if __name__ == "__main__":
    inp = [3, 0, 1]
    out = 2
    actual = Solution().missingNumber(inp)
    assert actual == out, (actual, out)

    inp = [9,6,4,2,3,5,7,0,1]
    out = 8
    actual = Solution().missingNumber(inp)
    assert actual == out, (actual, out)

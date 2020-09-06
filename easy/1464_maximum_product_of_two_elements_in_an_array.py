"""
Given the array of integers nums, you will choose two different indices i and j
of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
"""
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a, b = sorted(nums)[-2:]
        return (a - 1) * (b - 1)


if __name__ == "__main__":
    nums = [3, 4, 5, 2]
    out = 12
    res = Solution().maxProduct(nums)
    assert res == out, (res, out)

    nums = [1, 5, 4, 5]
    out = 16
    res = Solution().maxProduct(nums)
    assert res == out, (res, out)

    nums = [3, 7]
    out = 12
    res = Solution().maxProduct(nums)
    assert res == out, (res, out)

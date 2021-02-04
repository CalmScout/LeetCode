"""
We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.
Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.
A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing
the order of the remaining elements.

Constraints:
    * 1 <= nums.length <= 2 * 10^4
    * -10^9 <= nums[i] <= 10^9
"""
from typing import List
from collections import Counter


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = Counter(nums)
        res = 0
        for key in count:
            if key + 1 in count:
                res = max(res, count[key] + count[key + 1])
        return res


if __name__ == "__main__":
    nums = [1, 3, 2, 2, 5, 2, 3, 7]
    out = 5
    res = Solution().findLHS(nums)
    assert out == res, (out, res)

    nums = [1, 2, 3, 4]
    out = 2
    res = Solution().findLHS(nums)
    assert out == res, (out, res)

    nums = [1, 1, 1, 1]
    out = 0
    res = Solution().findLHS(nums)
    assert out == res, (out, res)

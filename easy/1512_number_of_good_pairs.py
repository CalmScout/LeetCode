"""
Given an array of integers nums.
A pair (i,j) is called good if nums[i] == nums[j] and i < j.
Return the number of good pairs.
"""
from typing import List
from collections import Counter


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = Counter(nums)
        res = 0
        for el in counter:
            if counter[el] > 1:
                res += counter[el] * (counter[el] - 1) // 2
        return res


if __name__ == "__main__":
    nums = [1, 2, 3, 1, 1, 3]
    out = 4
    res = Solution().numIdenticalPairs(nums)
    assert out == res, (out, res)

    nums = [1, 1, 1, 1]
    out = 6
    res = Solution().numIdenticalPairs(nums)
    assert out == res, (out, res)

    nums = [1, 2, 3]
    out = 0
    res = Solution().numIdenticalPairs(nums)
    assert out == res, (out, res)

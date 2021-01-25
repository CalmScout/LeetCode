"""
Given an array nums of 0s and 1s and an integer k, return True if all 1's are at least k places away
from each other, otherwise return False.
"""
from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        dist = k
        for el in nums:
            if el == 0:
                dist += 1
            if el == 1:
                if dist < k:
                    return False
                else:
                    dist = 0
        return True


if __name__ == "__main__":
    nums = [1, 0, 0, 0, 1, 0, 0, 1]
    k = 2
    out = True
    res = Solution().kLengthApart(nums, k)
    assert out == res, (out, res)

    nums = [1, 0, 0, 1, 0, 1]
    k = 2
    out = False
    res = Solution().kLengthApart(nums, k)
    assert out == res, (out, res)

    nums = [1, 1, 1, 1, 1]
    k = 0
    out = True
    res = Solution().kLengthApart(nums, k)
    assert out == res, (out, res)

    nums = [0, 1, 0, 1]
    k = 1
    out = True
    res = Solution().kLengthApart(nums, k)
    assert out == res, (out, res)

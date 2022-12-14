"""
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.
"""
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) > len(set(nums))


if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    out = True
    res = Solution().containsDuplicate(nums)
    assert res == out, (res, out)

    nums = [1, 2, 3, 4]
    out = False
    res = Solution().containsDuplicate(nums)
    assert res == out, (res, out)

    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    out = True
    res = Solution().containsDuplicate(nums)
    assert res == out, (res, out)
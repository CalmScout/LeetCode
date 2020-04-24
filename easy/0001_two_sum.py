"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        needed = {}
        for idx, el in enumerate(nums):
            if el in needed:
                return [needed[el], idx]
            else:
                key = target - el
                needed[key] = idx
        print(needed)
        return None


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    out = [0, 1]
    actual = Solution().twoSum(nums, target)
    assert out == actual, (out, actual)

"""
Given an array of size n, find the majority element. The majority element is the element
that appears more than ⌊ n/2 ⌋ times. You may assume that the array is non-empty and the
majority element always exist in the array.
"""
from typing import List
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        for el in counter:
            if counter[el] > len(nums) // 2:
                return el


if __name__ == "__main__":
    nums = [3, 2, 3]
    out = 3
    actual = Solution().majorityElement(nums)
    assert out == actual, (out, actual)

    nums = [2, 2, 1, 1, 1, 2, 2]
    out = 2
    actual = Solution().majorityElement(nums)
    assert out == actual, (out, actual)

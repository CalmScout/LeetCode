"""
Given an array of integers nums which is sorted in ascending order, and an integer target,
write a function to search target in nums. If target exists, then return its index.
Otherwise, return -1. You must write an algorithm with O(log n) runtime complexity.

Constraints:
    * 1 <= nums.length <= 104
    * -104 < nums[i], target < 104
    * All the integers in nums are unique.
    * nums is sorted in ascending order.
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pass


if __name__ == "__main__":
    nums = [-1,0,3,5,9,12]
    target = 9
    out = 4
    res = Solution().search(nums, target)
    assert out == res, (out, res)

    nums = [-1,0,3,5,9,12]
    target = 2
    out = -1
    res = Solution().search(nums, target)
    assert out == res, (out, res)

"""
Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most
twice and return the new length. Do not allocate extra space for another array, you must do this
by modifying the input array in-place with O(1) extra memory.
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums) - 1:
            j = i + 1
            while j < len(nums) and nums[i] == nums[j]:
                if j - i >= 2:
                    nums.pop(j)
                else:
                    j += 1
            i = j
        return len(nums)


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    out  = [1, 1, 2, 2, 3]
    Solution().removeDuplicates(nums)
    assert nums == out, (nums, out)

    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    out = [0, 0, 1, 1, 2, 3, 3]
    Solution().removeDuplicates(nums)
    assert nums == out, (nums, out)

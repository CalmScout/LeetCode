"""
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

Constraints:
    * 1 <= nums.length <= 104
    * -104 <= nums[i] <= 104
    * nums contains distinct values sorted in ascending order.
    * -104 <= target <= 104
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return(left)



if __name__ == "__main__":
    nums = [1,3,5,6]
    target = 5
    out = 2
    res = Solution().searchInsert(nums, target)
    assert out == res, (out, res)

    nums = [1,3,5,6]
    target = 2
    out = 1
    res = Solution().searchInsert(nums, target)
    assert out == res, (out, res)

    nums = [1,3,5,6]
    target = 7
    out = 4
    res = Solution().searchInsert(nums, target)
    assert out == res, (out, res)

    nums = [1,3,5,6]
    target = 0
    out = 0
    res = Solution().searchInsert(nums, target)
    assert out == res, (out, res)

    nums = [1]
    target = 0
    out = 0
    res = Solution().searchInsert(nums, target)
    assert out == res, (out, res)

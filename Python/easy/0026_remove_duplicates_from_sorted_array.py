"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates
in-place such that each unique element appears only once. The relative order of
the elements should be kept the same. Since it is impossible to change the length
of the array in some languages, you must instead have the result be placed in the
first part of the array nums. More formally, if there are k elements after removing
the duplicates, then the first k elements of nums should hold the final result. It
does not matter what you leave beyond the first k elements. Return k after placing
the final result in the first k slots of nums. Do not allocate extra space for
another array. You must do this by modifying the input array in-place with O(1)
extra memory.
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = len(nums)
        x = nums[0]
        # first go through the array and replace duplicates with None
        for i in range(1, k):
            if nums[i] == x:
                nums[i] = None
            else:
                x = nums[i]
        # clean up the array from np.inf in-place
        i = 0
        while i < k:
            if nums[i] is None:
                nums.pop(i)
                k -= 1
            else:
                i += 1
        return k


if __name__ == "__main__":
    nums = [1, 2, 3]
    out = 3
    res = Solution().removeDuplicates(nums)
    assert res == out
    assert nums[:res] == [1, 2, 3]

    nums = [1, 1, 2]
    out = 2
    res = Solution().removeDuplicates(nums)
    assert res == out
    assert nums[:res] == [1, 2]

    nums = [0,0,1,1,1,2,2,3,3,4]
    out = 5
    res = Solution().removeDuplicates(nums)
    assert res == out
    assert nums[:res] == [0,1,2,3,4]


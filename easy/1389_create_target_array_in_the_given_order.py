"""
Given two arrays of integers nums and index. Your task is to create target array under the following rules:
Initially target array is empty.
From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
Repeat the previous step until there are no elements to read in nums and index.
Return the target array.
It is guaranteed that the insertion operations will be valid.
"""
from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            result.insert(index[i], nums[i])
        return result


if __name__ == "__main__":
    nums = [0, 1, 2, 3, 4]
    index = [0, 1, 2, 2, 1]
    out = [0, 4, 1, 3, 2]
    actual = Solution().createTargetArray(nums, index)
    assert out == actual, (out, actual)

    nums = [1, 2, 3, 4, 0]
    index = [0, 1, 2, 3, 0]
    out = [0, 1, 2, 3, 4]
    actual = Solution().createTargetArray(nums, index)
    assert out == actual, (out, actual)

    nums = [1]
    index = [0]
    out = [1]
    actual = Solution().createTargetArray(nums, index)
    assert out == actual, (out, actual)

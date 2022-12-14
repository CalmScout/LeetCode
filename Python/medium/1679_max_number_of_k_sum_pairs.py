"""
You are given an integer array nums and an integer k.
In one operation, you can pick two numbers from the array whose sum equals
k and remove them from the array. Return the maximum number of operations
you can perform on the array.
"""
from typing import List
from collections import Counter


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        result = 0
        count = Counter(nums)
        for el in count:
            result += min(count[el], count[k - el])
        return result // 2


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    k = 5
    out = 2
    res = Solution().maxOperations(nums, k)
    assert out == res, (out, res)

    nums = [3, 1, 3, 4, 3]
    k = 6
    out = 1
    res = Solution().maxOperations(nums, k)
    assert out == res, (out, res)

    nums = [2, 2, 2, 3, 1, 1, 4, 1]
    k = 4
    out = 2
    res = Solution().maxOperations(nums, k)
    assert out == res, (out, res)

    nums = [2, 5, 4, 4, 1, 3, 4, 4, 1, 4, 4, 1, 2, 1, 2, 2, 3, 2, 4, 2]
    k = 3
    out = 4
    res = Solution().maxOperations(nums, k)
    assert out == res, (out, res)

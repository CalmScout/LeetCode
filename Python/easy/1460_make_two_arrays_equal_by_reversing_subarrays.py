"""
Given two integer arrays of equal length target and arr. In one step,
you can select any non-empty sub-array of arr and reverse it. You are
allowed to make any number of steps. Return True if you can make arr
equal to target, or False otherwise.
"""
from typing import List
from collections import Counter


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return Counter(target) == Counter(arr)


if __name__ == "__main__":
    target = [1, 2, 3, 4]
    arr = [2, 4, 1, 3]
    out = True
    res = Solution().canBeEqual(target, arr)
    assert res == out, (res, out)

    target = [7]
    arr = [7]
    out = True
    res = Solution().canBeEqual(target, arr)
    assert res == out, (res, out)

    target = [1, 12]
    arr = [12, 1]
    out = True
    res = Solution().canBeEqual(target, arr)
    assert res == out, (res, out)

    target = [3, 7, 9]
    arr = [3, 7, 11]
    out = False
    res = Solution().canBeEqual(target, arr)
    assert res == out, (res, out)

    target = [1, 1, 1, 1, 1]
    arr = [1, 1, 1, 1, 1]
    out = True
    res = Solution().canBeEqual(target, arr)
    assert res == out, (res, out)
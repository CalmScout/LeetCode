"""
Given an array of numbers arr. A sequence of numbers is called an arithmetic progression
if the difference between any two consecutive elements is the same.
Return true if the array can be rearranged to form an arithmetic progression, otherwise,
return false.
"""
from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        dx = arr[1] - arr[0]
        for idx in range(2, len(arr)):
            if arr[idx] - arr[idx - 1] != dx:
                return False
        return True


if __name__ == "__main__":
    arr = [3, 5, 1]
    out = True
    res = Solution().canMakeArithmeticProgression(arr)
    assert res == out, (res, out)

    arr = [1, 2, 4]
    out = False
    res = Solution().canMakeArithmeticProgression(arr)
    assert res == out, (res, out)

"""
Given an array arr, replace every element in that array with the greatest element among the
elements to its right, and replace the last element with -1.
After doing so, return the array.
"""
from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return [-1]
        elif len(arr) == 2:
            return [arr[0], -1]
        result = [-1] * len(arr)
        result[-2] = arr[-1]
        for i in range(len(arr) - 3, -1, -1):
            result[i] = max(arr[i+1], result[i+1])
        return result


if __name__ == "__main__":
    arr = [17, 18, 5, 4, 6, 1]
    out = [18, 6, 6, 6, 1, -1]
    actual = Solution().replaceElements(arr)
    assert out == actual, (out, actual)

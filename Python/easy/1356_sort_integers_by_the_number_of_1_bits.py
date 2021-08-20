"""
Given an integer array arr. You have to sort the integers in the array in ascending order by the number of 1's
in their binary representation and in case of two or more integers have the same number of 1's you have to sort
them in ascending order. Return the sorted array.

Constraints:
    * 1 <= arr.length <= 500
    * 0 <= arr[i] <= 10^4
"""
from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        result = sorted(arr, key=lambda x: (bin(x).count("1"), x))
        return result


if __name__ == "__main__":
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    out = [0, 1, 2, 4, 8, 3, 5, 6, 7]
    res = Solution().sortByBits(arr)
    assert res == out, (res, out)

    arr = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
    out = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    res = Solution().sortByBits(arr)
    assert res == out, (res, out)

    arr = [10000, 10000]
    out = [10000, 10000]
    res = Solution().sortByBits(arr)
    assert res == out, (res, out)

    arr = [2, 3, 5, 7, 11, 13, 17, 19]
    out = [2, 3, 5, 17, 7, 11, 13, 19]
    res = Solution().sortByBits(arr)
    assert res == out, (res, out)

    arr = [10, 100, 1000, 10000]
    out = [10, 100, 10000, 1000]
    res = Solution().sortByBits(arr)
    assert res == out, (res, out)

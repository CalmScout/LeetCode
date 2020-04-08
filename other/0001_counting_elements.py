"""
Given an integer array arr, count element x such that x + 1 is also in arr.
If there're duplicates in arr, count them seperately.
"""
from typing import List
import collections


class Solution:
    def countElements(self, arr: List[int]) -> int:
        result = 0
        counter = collections.Counter(arr)
        keys = sorted(list(counter.keys()))
        for key in keys[:-1]:
            if key + 1 in keys:
                result += counter[key]
        return result


if __name__ == "__main__":
    arr = [1, 2, 3]
    out = 2 # Explanation: 1 and 2 are counted cause 2 and 3 are in arr.
    actual = Solution().countElements(arr)
    assert out == actual, (out, actual)

    arr = [1, 1, 3, 3, 5, 5, 7, 7]
    out = 0 # Explanation: No numbers are counted, cause there's no 2, 4, 6, or 8 in arr.
    actual = Solution().countElements(arr)
    assert out == actual, (out, actual)

    arr = [1, 3, 2, 3, 5, 0]
    out = 3 # Explanation: 0, 1 and 2 are counted cause 1, 2 and 3 are in arr.
    actual = Solution().countElements(arr)
    assert out == actual, (out, actual)

    arr = [1, 1, 2, 2]
    out = 2 # Explanation: Two 1s are counted cause 2 is in arr.
    actual = Solution().countElements(arr)
    assert out == actual, (out, actual)

    arr = [1, 1, 2]
    out = 2
    actual = Solution().countElements(arr)
    assert out == actual, (out, actual)
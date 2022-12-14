"""
Given an array of positive integers arr, calculate the sum of all possible odd-length subarrays.
A subarray is a contiguous subsequence of the array.
Return the sum of all odd-length subarrays of arr.

Constraints:
    * 1 <= arr.length <= 100
    * 1 <= arr[i] <= 1000
"""
from typing import List
import numpy as np


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        result = 0
        arr_np = np.array(arr)
        for k in range(1, len(arr), 2):
            for i in range(len(arr) - k + 1):
                result += sum(arr_np[i : (i+k)])
        if len(arr_np) % 2 == 1:
            result += sum(arr_np)
        return result


if __name__ == "__main__":
    arr = [1,4,2,5,3]
    out = 58
    res = Solution().sumOddLengthSubarrays(arr)
    assert res == out, (res, out)

    arr = [1,2]
    out = 3
    res = Solution().sumOddLengthSubarrays(arr)
    assert res == out, (res, out)

    arr = [10,11,12]
    out = 66
    res = Solution().sumOddLengthSubarrays(arr)
    assert res == out, (res, out)

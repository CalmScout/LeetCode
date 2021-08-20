"""
Given an array arr of integers, check if there exists two integers N and M such that N
is the double of M ( i.e. N = 2 * M).

More formally check if there exists two indices i and j such that :
    * i != j
    * 0 <= i, j < arr.length
    * arr[i] == 2 * arr[j]

Constraints:
    * 2 <= arr.length <= 500
    * -10^3 <= arr[i] <= 10^3
"""
from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        d = {}
        for el in arr:
            if el*2 in d or el/2 in d:
                return  True
            else:
                d[el] = 42
        return False


if __name__ == "__main__":
    arr = [10,2,5,3]
    out = True
    res = Solution().checkIfExist(arr)
    assert out == res, (out, res)

    arr = [7,1,14,11]
    out = True
    res = Solution().checkIfExist(arr)
    assert out == res, (out, res)

    arr = [3,1,7,11]
    out = False
    res = Solution().checkIfExist(arr)
    assert out == res, (out, res)

    arr = [2,3,3,0,0]
    out = True
    res = Solution().checkIfExist(arr)
    assert out == res, (out, res)

    arr = [-2,0,10,-19,4,6,-8]
    out = False
    res = Solution().checkIfExist(arr)
    assert out == res, (out, res)

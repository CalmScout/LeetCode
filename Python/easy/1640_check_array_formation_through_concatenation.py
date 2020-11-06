"""
You are given an array of distinct integers arr and an array of integer arrays pieces,
where the integers in pieces are distinct. Your goal is to form arr by concatenating the
arrays in pieces in any order. However, you are not allowed to reorder the integers in
each array pieces[i]. Return true if it is possible to form the array arr from pieces.
Otherwise, return false.
"""
from typing import List


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        d = {p[0]: p for p in pieces}
        res = []
        for num in arr:
            res += d.get(num, [])
        return res == arr


if __name__ == "__main__":
    arr = [85]
    pieces = [[85]]
    out = True
    res = Solution().canFormArray(arr, pieces)
    assert out == res, (out, res)

    arr = [15, 88]
    pieces = [[88], [15]]
    out = True
    res = Solution().canFormArray(arr, pieces)
    assert out == res, (out, res)

    arr = [91, 4, 64, 78]
    pieces = [[78], [4, 64], [91]]
    out = True
    res = Solution().canFormArray(arr, pieces)
    assert out == res, (out, res)

    arr = [1, 3, 5, 7]
    pieces = [[2, 4, 6, 8]]
    out = False
    res = Solution().canFormArray(arr, pieces)
    assert out == res, (out, res)

    arr = [49, 18, 16]
    pieces = [[16, 18, 49]]
    out = False
    res = Solution().canFormArray(arr, pieces)
    assert out == res, (out, res)

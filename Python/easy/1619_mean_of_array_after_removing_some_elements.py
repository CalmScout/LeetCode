"""
Given an integer array arr, return the mean of the remaining integers after
removing the smallest 5% and the largest 5% of the elements.
Answers within 10-5 of the actual answer will be considered accepted.
"""
from typing import List


class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n = int(.05 * len(arr))
        return sum(arr[n:(-n)]) / (len(arr)*.9)


if __name__ == "__main__":
    EPS = 1e-5
    
    arr = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,\
         2, 2, 2, 2, 2, 2, 2, 3]
    out = 2.0
    res = Solution().trimMean(arr)
    assert res > out - EPS and res < out + EPS

    arr = [6, 2, 7, 5, 1, 2, 0, 3, 10, 2, 5, 0,\
         5, 5, 0, 8, 7, 6, 8, 0]
    out = 4.0
    res = Solution().trimMean(arr)
    assert res > out - EPS and res < out + EPS

    arr = [6, 0, 7, 0, 7, 5, 7, 8, 3, 4, 0, 7, 8,\
        1, 6, 8, 1, 1, 2, 4, 8, 1, 9, 5, 4, 3, 8,\
        5, 10, 8, 6, 6, 1, 0, 6, 10, 8, 2, 3, 4]
    out = 4.77778
    res = Solution().trimMean(arr)
    assert res > out - EPS and res < out + EPS

    arr = [9, 7, 8, 7, 7, 8, 4, 4, 6, 8, 8, 7, 6,\
        8, 8, 9, 2, 6, 0, 0, 1, 10, 8, 6, 3, 3, 5,\
        1, 10, 9, 0, 7, 10, 0, 10, 4, 1, 10, 6, 9,\
        3, 6, 0, 0, 2, 7, 0, 6, 7, 2, 9, 7, 7, 3, 0,\
        1, 6, 1, 10, 3]
    out = 5.27778
    res = Solution().trimMean(arr)
    assert res > out - EPS and res < out + EPS

    arr = [4, 8, 4, 10, 0, 7, 1, 3, 7, 8, 8, 3, 4, 1,\
        6, 2, 1, 1, 8, 0, 9, 8, 0, 3, 9, 10, 3, 10, 1,\
        10, 7, 3, 2, 1, 4, 9, 10, 7, 6, 4, 0, 8, 5, 1,\
        2, 1, 6, 2, 5, 0, 7, 10, 9, 10, 3, 7, 10, 5, 8,\
        5, 7, 6, 7, 6, 10, 9, 5, 10, 5, 5, 7, 2, 10, 7,\
        7, 8, 2, 0, 1, 1]
    out = 5.29167
    res = Solution().trimMean(arr)
    assert res > out - EPS and res < out + EPS

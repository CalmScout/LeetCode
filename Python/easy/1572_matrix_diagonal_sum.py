"""
Given a square matrix mat, return the sum of the matrix diagonals.
Only include the sum of all the elements on the primary diagonal and all
the elements on the secondary diagonal that are not part of the primary diagonal.
"""
from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0
        for i in range(len(mat)):
            res += mat[i][i] + mat[i][-1 - i]
        if len(mat) % 2 == 1:
            res -= mat[len(mat) // 2][len(mat) // 2]
        return res


if __name__ == "__main__":
    mat = [[1,2,3],
           [4,5,6],
           [7,8,9]]
    out = 25
    res = Solution().diagonalSum(mat)
    assert out == res, (out, res)

    mat = [[1,1,1,1],
           [1,1,1,1],
           [1,1,1,1],
           [1,1,1,1]]
    out = 8
    res = Solution().diagonalSum(mat)
    assert out == res, (out, res)

    mat = [[5]]
    out = 5
    res = Solution().diagonalSum(mat)
    assert out == res, (out, res)

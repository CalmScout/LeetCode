"""
Given n and m which are the dimensions of a matrix initialized by zeros and given an array indices
where indices[i] = [ri, ci]. For each pair of [ri, ci] you have to increment all cells in row ri
and column ci by 1.
Return the number of cells with odd values in the matrix after applying the increment to all indices.
"""
from typing import List

class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        rows_count = [0] * n
        cols_count = [0] * m
        for el in indices:
            rows_count[el[0]] += 1
            cols_count[el[1]] += 1
        result = 0
        for i in range(n):
            for j in range(m):
                if (rows_count[i] + cols_count[j]) % 2 == 1:
                    result += 1
        return result


if __name__ == "__main__":
    n = 2
    m = 3
    indices = [[0, 1], [1, 1]]
    out = 6
    actual = Solution().oddCells(n, m, indices)
    assert actual == out, (actual, out)

    n = 2
    m = 2
    indices = [[1, 1], [0, 0]]
    out = 0
    actual = Solution().oddCells(n, m, indices)
    assert actual == out, (actual, out)

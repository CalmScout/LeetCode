"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach
the bottom-right corner of the grid (marked 'Finish' in the diagram below).
How many possible unique paths are there?
Note: m and n will be at most 100.
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        grid = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            grid[i][0] = 1
        for j in range(n):
            grid[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]
        return grid[m-1][n-1]


if __name__ == "__main__":
    m, n = 3, 2
    out = 3
    actual = Solution().uniquePaths(m, n)
    assert actual == out, (actual, out)

    m, n = 7, 3
    out = 28
    actual = Solution().uniquePaths(m, n)
    assert actual == out, (actual, out)

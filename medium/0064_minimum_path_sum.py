"""
Given a m x n grid filled with non-negative numbers, find a path from top
left to bottom right which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.
"""
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # initialize dynamic programming array
        dp = []
        for i in range(m):
            dp.append([0 for _ in range(n)])
        # filling dp array: initialization
        dp[m-1][n-1] = grid[m-1][n-1]
        for i in range(m-2, -1, -1):
            dp[i][n-1] = grid[i][n-1] + dp[i+1][n-1]
        for j in range(n-2, -1, -1):
            dp[m-1][j] = grid[m-1][j] + dp[m-1][j+1]
        # filling dp array: main cycle
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                dp[i][j] = grid[i][j] + min(dp[i+1][j], dp[i][j+1])
        return dp[0][0]


if __name__ == "__main__":
    inp = [[1,3,1],
           [1,5,1],
           [4,2,1]
        ]
    out = 7
    # Explanation: Because the path 1→3→1→1→1 minimizes the sum.
    actual = Solution().minPathSum(inp)
    assert actual == out, (actual, out)

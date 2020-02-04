"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach
the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?
An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.
"""
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if (n == 1 or m == 1) and sum([sum(x) for x in obstacleGrid]):
            return 0
        #initialization
        grid = [[0 for i in range(n)] for j in range(m)]
        for j in range(n):
            if obstacleGrid[0][j] == 0:
                grid[0][j] = 1
            else:
                break
        for i in range(m):
            if obstacleGrid[i][0] == 0:
                grid[i][0] = 1
            else:
                break
        # fill in `grid`
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    grid[i][j] = 0
                else:
                    grid[i][j] = grid[i-1][j] + grid[i][j-1]
        return grid[-1][-1]


if __name__ == "__main__":
    inp = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    out = 2
    actual = Solution().uniquePathsWithObstacles(inp)
    assert actual == out, (actual, out)

    inp = [
        [0, 1, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    out = 1
    actual = Solution().uniquePathsWithObstacles(inp)
    assert actual == out, (actual, out)

    inp = [[1, 0]]
    out = 0
    actual = Solution().uniquePathsWithObstacles(inp)
    assert actual == out, (actual, out)

    inp = [[1, 0], [0, 0]]
    out = 0
    actual = Solution().uniquePathsWithObstacles(inp)
    assert actual == out, (actual, out)

    # inp = [[0, 0], [1, 1], [0, 0]]
    # out = 0
    # actual = Solution().uniquePathsWithObstacles(inp)
    # assert actual == out, (actual, out)

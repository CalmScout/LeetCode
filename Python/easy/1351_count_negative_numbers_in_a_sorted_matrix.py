"""
Given a m * n matrix grid which is sorted in non-increasing
order both row-wise and column-wise.
Return the number of negative numbers in grid.
"""
from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        counter = 0
        for i in range(len(grid)-1, -1, -1):
            for j in range(len(grid[0])-1, -1, -1):
                if grid[i][j] < 0:
                    counter += 1
                else:
                    break
        return counter


if __name__ == "__main__":
    grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
    out = 8
    res = Solution().countNegatives(grid)
    assert res == out, (res, out)

    grid = [[3,2],[1,0]]
    out = 0
    res = Solution().countNegatives(grid)
    assert res == out, (res, out)

    grid = [[1,-1],[-1,-1]]
    out = 3
    res = Solution().countNegatives(grid)
    assert res == out, (res, out)

    grid = [[-1]]
    out = 1
    res = Solution().countNegatives(grid)
    assert res == out, (res, out)

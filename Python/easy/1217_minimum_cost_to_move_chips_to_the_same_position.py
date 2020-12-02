"""
We have n chips, where the position of the ith chip is position[i].
We need to move all the chips to the same position. In one step, we
can change the position of the ith chip from position[i] to:
position[i] + 2 or position[i] - 2 with cost = 0.
position[i] + 1 or position[i] - 1 with cost = 1.
Return the minimum cost needed to move all the chips to the same
position.
"""
from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        even_count = 0
        odd_count = 0
        for el in position:
            if el % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
        return min(even_count, odd_count)


if __name__ == "__main__":
    position = [1, 2, 3]
    out = 1
    res = Solution().minCostToMoveChips(position)
    assert out == res, (out, res)

    position = [2, 2, 2, 3, 3]
    out = 2
    res = Solution().minCostToMoveChips(position)
    assert out == res, (out, res)

    position = [1, 1000000000]
    out = 1
    res = Solution().minCostToMoveChips(position)
    assert out == res, (out, res)

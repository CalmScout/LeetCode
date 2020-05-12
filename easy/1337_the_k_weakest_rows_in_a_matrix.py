"""
Given a m * n matrix mat of ones (representing soldiers) and zeros (representing civilians),
return the indexes of the k weakest rows in the matrix ordered from the weakest to the strongest.
A row i is weaker than row j, if the number of soldiers in row i is less than the number of
soldiers in row j, or they have the same number of soldiers but i is less than j. Soldiers are
always stand in the frontier of a row, that is, always ones may appear first and then zeros.
"""
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        sums = [sum(x) for x in mat]
        pairs = [(idx, val) for idx, val in enumerate(sums)]
        pairs = sorted(pairs, key=lambda x: x[1])
        result = [x[0] for x in pairs[:k]]
        return result


if __name__ == "__main__":
    mat = [[1, 1, 0, 0, 0],
           [1, 1, 1, 1, 0],
           [1, 0, 0, 0, 0],
           [1, 1, 0, 0, 0],
           [1, 1, 1, 1, 1]]
    k = 3
    out = [2, 0, 3]
    actual = Solution().kWeakestRows(mat, k)
    assert out == actual, (out, actual)
    # Explanation:
    # The number of soldiers for each row is: 
    # row 0 -> 2 
    # row 1 -> 4 
    # row 2 -> 1 
    # row 3 -> 2 
    # row 4 -> 5 
    # Rows ordered from the weakest to the strongest are [2,0,3,1,4]

    mat = [[1, 0, 0, 0],
           [1, 1, 1, 1],
           [1, 0, 0, 0],
           [1, 0, 0, 0]]
    k = 2
    out = [0, 2]
    actual = Solution().kWeakestRows(mat, k)
    assert out == actual, (out, actual)
    # Explanation: 
    # The number of soldiers for each row is: 
    # row 0 -> 1 
    # row 1 -> 4 
    # row 2 -> 1 
    # row 3 -> 1 
    # Rows ordered from the weakest to the strongest are [0,2,3,1]

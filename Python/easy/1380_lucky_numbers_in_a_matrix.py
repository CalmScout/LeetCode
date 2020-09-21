"""
Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.
A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

Example 1:
Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column

Example 2:
Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
Output: [12]
Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.

Example 3:
Input: matrix = [[7,8],[1,2]]
Output: [7]
 

Constraints:
m == mat.length
n == mat[i].length
1 <= n, m <= 50
1 <= matrix[i][j] <= 10^5.
All elements in the matrix are distinct.
"""
from typing import List


class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        # pre-compute min in rows and max in columns values
        min_rows = {min(el) for el in matrix}

        def get_row_max(matrix: List[List[int]], col_idx:int) -> int:
            result = matrix[0][col_idx]
            if len(matrix) == 1:
                return result
            for i in range(1, len(matrix)):
                if matrix[i][col_idx] > result:
                    result = matrix[i][col_idx]
            return result
        
        max_cols = {get_row_max(matrix, idx) for idx in range(n)}

        result = list(min_rows.intersection(max_cols))
        return result


if __name__ == "__main__":
    matrix = [[3,7,8],[9,11,13],[15,16,17]]
    out = [15]
    actual = Solution().luckyNumbers(matrix)
    assert out == actual, (out, actual)

    matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
    out = [12]
    actual = Solution().luckyNumbers(matrix)
    assert out == actual, (out, actual)

    matrix = [[7,8],[1,2]]
    out = [7]
    actual = Solution().luckyNumbers(matrix)
    assert out == actual, (out, actual)

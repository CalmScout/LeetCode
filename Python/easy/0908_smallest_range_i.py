"""
Given an array A of integers, for each integer A[i] we may choose any x with -K <= x <= K,
and add x to A[i]. After this process, we have some array B. Return the smallest possible
difference between the maximum value of B and the minimum value of B.

Example 1:
Input: A = [1], K = 0
Output: 0
Explanation: B = [1]

Example 2:
Input: A = [0,10], K = 2
Output: 6
Explanation: B = [2,8]

Example 3:
Input: A = [1,3,6], K = 3
Output: 0
Explanation: B = [3,3,3] or B = [4,4,4]

Note:
1 <= A.length <= 10000
0 <= A[i] <= 10000
0 <= K <= 10000
"""
import statistics
from typing import List


class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        ma, mi = max(A), min(A)
        return 0 if (ma - mi) < (2*K) else ma - mi - (2 * K)


if __name__ == "__main__":
    A = [1]
    K = 0
    out = 0
    actual = Solution().smallestRangeI(A, K)
    assert  actual == out, (actual, out)

    A = [0, 10]
    K = 2
    out = 6 
    actual = Solution().smallestRangeI(A, K)
    assert  actual == out, (actual, out)

    A = [1, 3, 6]
    K = 3
    out = 0
    actual = Solution().smallestRangeI(A, K)
    assert  actual == out, (actual, out)

    A = [9, 10, 0, 7]
    K = 1
    out = 8
    actual = Solution().smallestRangeI(A, K)
    assert  actual == out, (actual, out)

    A = [3, 1, 10]
    K = 4
    out = 1
    actual = Solution().smallestRangeI(A, K)
    assert  actual == out, (actual, out)

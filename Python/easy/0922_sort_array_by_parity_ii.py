"""
Given an array A of non-negative integers, half of the integers in A are odd, and half of
the integers are even. Sort the array so that whenever A[i] is odd, i is odd; and whenever
A[i] is even, i is even.

You may return any answer array that satisfies this condition.

 

Example 1:

Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
 
Note:
2 <= A.length <= 20000
A.length % 2 == 0
0 <= A[i] <= 1000
"""
from typing import List


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        even = []
        odd = []
        for el in A:
            if el % 2 == 0:
                even.append(el)
            else:
                odd.append(el)
        result = []
        for i in range(len(even)):
            result.append(even[i])
            result.append(odd[i])
        return result


if __name__ == "__main__":
    inp = [4, 2, 5, 7]
    out = Solution().sortArrayByParityII(inp)
    assert out in [[4, 5, 2, 7], [4, 7, 2, 5], [2, 5, 4, 7], [2, 7, 4, 5]]

"""
Let's call an array A a mountain if the following properties hold:
1) A.length >= 3
2) There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > 
A[i+1] > ... > A[A.length - 1].

Example 1:
Input: [0,1,0]
Output: 1

Example 2:
Input: [0,2,1,0]
Output: 1
Note:

3 <= A.length <= 10000
0 <= A[i] <= 10^6
A is a mountain, as defined above.
"""
from typing import List


class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        if not A:
            return
        
        left, right = 1, len(A) - 2
        while left + 1 < right:
            mid = (left + right) // 2
            if A[mid] < A[mid - 1]:
                right = mid
            elif A[mid] < A[mid + 1]:
                left = mid
            else:
                left = mid
        
        if A[left] > A[right]:
            return left
        return right


if __name__ == "__main__":
    assert Solution().peakIndexInMountainArray([0, 1, 0]) == 1
    assert Solution().peakIndexInMountainArray([0, 2, 1, 0]) == 1

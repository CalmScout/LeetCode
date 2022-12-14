"""
Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.

Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:

If S[i] == "I", then A[i] < A[i+1]
If S[i] == "D", then A[i] > A[i+1]

Example 1:
Input: "IDID"
Output: [0,4,1,3,2]

Example 2:
Input: "III"
Output: [0,1,2,3]

Example 3:
Input: "DDI"
Output: [3,2,0,1]
 

Note:
1 <= S.length <= 10000
S only contains characters "I" or "D".
"""
from typing import List

class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        left = 0
        right = len(S)
        result = [None] * (right + 1)
        for idx, el in enumerate(S):
            if el == "I":
                result[idx] = left
                left += 1
            else:
                result[idx] = right
                right -= 1
        result[-1] = left
        return result


if __name__ == "__main__":
    assert Solution().diStringMatch("IDID") == [0,4,1,3,2]
    assert Solution().diStringMatch("III") == [0,1,2,3]
    assert Solution().diStringMatch("DDI") == [3,2,0,1]

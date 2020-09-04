"""
Given a string s and an integer array indices of the same length. The string s will
be shuffled such that the character at the ith position moves to indices[i] in the
shuffled string. Return the shuffled string.
"""
from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(s)
        a = [None] * n
        for i, idx in enumerate(indices):
            a[idx] = s[i]
        return ''.join(a)


if __name__ == "__main__":
    s = "codeleet"
    indices = [4,5,6,7,0,2,1,3]
    out = "leetcode"
    res = Solution().restoreString(s, indices)
    assert res == out, (res, out)

    s = "abc"
    indices = [0, 1, 2]
    out = "abc"
    res = Solution().restoreString(s, indices)
    assert res == out, (res, out)

    s = "aiohn"
    indices = [3,1,4,2,0]
    out = "nihao"
    res = Solution().restoreString(s, indices)
    assert res == out, (res, out)

    s = "aaiougrt"
    indices = [4,0,2,6,7,3,1,5]
    out = "arigatou"
    res = Solution().restoreString(s, indices)
    assert res == out, (res, out)

    s = "art"
    indices = [1, 0, 2]
    out = "rat"
    res = Solution().restoreString(s, indices)
    assert res == out, (res, out)

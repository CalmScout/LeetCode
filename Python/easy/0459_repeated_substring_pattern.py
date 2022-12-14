"""
Given a non-empty string check if it can be constructed by taking a substring
of it and appending multiple copies of the substring together. You may assume
the given string consists of lowercase English letters only and its length
will not exceed 10000.
"""
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for n in range(1, len(s)//2 + 1):
            if len(s) % n == 0:
                times = len(s) // n
                if s[:n] * times == s:
                    return True
        return False


if __name__ == "__main__":
    inp = "abab"
    out = True
    res = Solution().repeatedSubstringPattern(inp)
    assert res == out, (res, out)

    inp = "aba"
    out = False
    res = Solution().repeatedSubstringPattern(inp)
    assert res == out, (res, out)

    inp = "abcabcabcabc"
    out = True
    res = Solution().repeatedSubstringPattern(inp)
    assert res == out, (res, out)

    inp = "bb"
    out = True
    res = Solution().repeatedSubstringPattern(inp)
    assert res == out, (res, out)

"""
Given a string s, return the longest palindromic substring in s.
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        while l > 1:
            for start in range(len(s) - l + 1):
                candidate = s[start:(start + l)]
                if candidate == candidate[::-1]:
                    return candidate
            l -= 1
        return s[0]


if __name__ == "__main__":
    s = "babad"
    out = "bab"
    res = Solution().longestPalindrome(s)
    assert out == res, (out, res)

    s = "cbbd"
    out = "bb"
    res = Solution().longestPalindrome(s)
    assert out == res, (out, res)

    s = "a"
    out = "a"
    res = Solution().longestPalindrome(s)
    assert out == res, (out, res)

    s = "ac"
    out = "a"
    res = Solution().longestPalindrome(s)
    assert out == res, (out, res)

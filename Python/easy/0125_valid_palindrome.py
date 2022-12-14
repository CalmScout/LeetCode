"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase
letters and removing all non-alphanumeric characters, it reads the same forward and
backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
"""
import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        regex = re.compile('[^a-z0-9]')
        res = regex.sub('', s)
        return res == res[::-1]


if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    res = Solution().isPalindrome(s)
    out = True
    assert out == res, res

    s = "race a car"
    res = Solution().isPalindrome(s)
    out = False
    assert out == res, res

    s = " "
    res = Solution().isPalindrome(s)
    out = True
    assert out == res, res

    s = "0P"
    res = Solution().isPalindrome(s)
    out = False
    assert out == res, res

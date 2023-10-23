"""
Given two strings needle and haystack, return the index of the first occurrence
of needle in haystack, or -1 if needle is not part of haystack.
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # return haystack.find(needle)
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle: return i
        return -1


if __name__ == '__main__':
    haystack = "sadbutsad"
    needle = "sad"
    res = Solution().strStr(haystack, needle)
    assert res == 0, f'Expected 0, got {res}'

    haystack = "leetcode"
    needle = "leeto"
    res = Solution().strStr(haystack, needle)
    assert res == -1, f'Expected -1, got {res}'

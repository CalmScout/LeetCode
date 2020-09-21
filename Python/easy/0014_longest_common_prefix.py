"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        len_res = 0
        len_min = min(map(len, strs))
        passed = True
        while passed and len_res <= len_min:
            len_res += 1
            template = strs[0][0:len_res]
            for word in strs[1:]:
                if word[:len_res] != template:
                    passed = False
                    break
        if passed:
            return strs[0][0:len_res]
        else:
            return strs[0][0:(len_res - 1)]


if __name__ == "__main__":
    strs = ["flower","flow","flight"]
    out = "fl"
    actual = Solution().longestCommonPrefix(strs)
    assert actual == out, (actual, out)

    strs = ["dog","racecar","car"]
    out = ""
    actual = Solution().longestCommonPrefix(strs)
    assert actual == out, (actual, out)

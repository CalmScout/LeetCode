"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means
the last appearing word if we loop from left to right) in the string. If the last word does not exist, return 0.
Note: A word is defined as a maximal substring consisting of non-space characters only.
"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(" ")[-1])


if __name__ == "__main__":
    inp = "Hello World"
    out = 5
    actual = Solution().lengthOfLastWord(inp)
    assert actual == out, (actual, out)

    inp = "a "
    out = 1
    actual = Solution().lengthOfLastWord(inp)
    assert actual == out, (actual, out)

"""
Given a string, you need to reverse the order of characters in each word within a sentence while still
preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in
the string.
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        result = [word[::-1] for word in words]
        return " ".join(result)


if __name__ == "__main__":
    inp = "Let's take LeetCode contest"
    out = "s'teL ekat edoCteeL tsetnoc"
    assert Solution().reverseWords(inp) == out, (inp, out)

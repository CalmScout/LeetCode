"""
Write a function that reverses a string. The input string is given as an array of characters char[].
Do not allocate extra space for another array, you must do this by modifying the input array
in-place with O(1) extra memory. You may assume all the characters consist of printable ascii
characters.

Example 1:
Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if not s or len(s) == 0:
            return
        for idx in range(len(s) // 2):
            s[idx], s[-1 - idx] = s[-1 - idx], s[idx]


if __name__ == "__main__":
    inp = ["h","e","l","l","o"]
    Solution().reverseString(inp)
    out = ["o","l","l","e","h"]
    assert inp == out
    inp = ["H","a","n","n","a","h"]
    Solution().reverseString(inp)
    out = ["h","a","n","n","a","H"]
    assert inp == out

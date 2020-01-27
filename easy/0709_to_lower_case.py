"""
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

Example 1:
Input: "Hello"
Output: "hello"

Example 2:
Input: "here"
Output: "here"

Example 3:
Input: "LOVELY"
Output: "lovely"
"""
class Solution:
    def toLowerCase(self, str: str) -> str:
        return str.lower()


if __name__ == "__main__":
    assert Solution().toLowerCase("Hello") == "hello"
    assert Solution().toLowerCase("here") == "here"
    assert Solution().toLowerCase("LOVELY") == "lovely"

"""
Given two binary strings a and b, return their sum as a binary string.
Constraints:
    * 1 <= a.length, b.length <= 104
    * a and b consist only of '0' or '1' characters.
    * Each string does not contain leading zeros except for the zero itself.
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]


if __name__ == "__main__":
    a = "11"
    b = "1"
    out = "100"
    res = Solution().addBinary(a, b)
    assert out == res, (out, res)

    a = "1010"
    b = "1011"
    out = "10101"
    res = Solution().addBinary(a, b)
    assert out == res, (out, res)

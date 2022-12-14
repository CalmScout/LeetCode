"""
The Hamming distance between two integers is the number of positions at which
the corresponding bits are different. Given two integers x and y, calculate
the Hamming distance.

Note:
0 ≤ x, y < 2**31.
"""
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count("1")


if __name__ == "__main__":
    x = 1
    y = 4
    out = 2
    actual = Solution().hammingDistance(x, y)
    assert actual == out, (actual, out)

    x = 3
    y = 1
    out = 1
    actual = Solution().hammingDistance(x, y)
    assert actual == out, (actual, out)

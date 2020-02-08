"""
Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment which could only store integers within the
32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume
that your function returns 0 when the reversed integer overflows.
"""
class Solution:
    def reverse(self, x: int) -> int:
        x_str = str(x)
        sign = ""
        if x_str[0] == "-":
            sign = "-"
            x_str = x_str[1:]
        result = int(sign + x_str[::-1])
        if result > 2 ** 31 - 1 or result < -2**31:
            return 0
        return result


if __name__ == "__main__":
    inp = 123
    out = 321
    actual = Solution().reverse(inp)
    assert out == actual, (out, actual)

    inp = -123
    out = -321
    actual = Solution().reverse(inp)
    assert out == actual, (out, actual)

    inp = 120
    out = 21
    actual = Solution().reverse(inp)
    assert out == actual, (out, actual)

    inp = 1534236469
    out = 0
    actual = Solution().reverse(inp)
    assert out == actual, (out, actual)

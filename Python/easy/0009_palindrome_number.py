"""
Determine whether an integer is a palindrome. An integer is a palindrome when it
reads the same backward as forward.
Solve it without converting the integer to a string.
"""
import math


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
        digits = int(math.log10(x)) + 1
        left_div = 10 ** (digits - 1)
        right_div = 10
        for _ in range(digits // 2):
            first = x // left_div
            last = x % 10
            if first != last:
                return False
            x %= left_div
            x //= 10
            left_div /= 100
        return True


if __name__ == "__main__":
    inp = 121
    out = True
    actual = Solution().isPalindrome(inp)
    assert out == actual, (out, actual)

    inp = -121
    out = False
    actual = Solution().isPalindrome(inp)
    assert out == actual, (out, actual)

    inp = 10
    out = False
    actual = Solution().isPalindrome(inp)
    assert out == actual, (out, actual)

    inp = 8
    out = True
    actual = Solution().isPalindrome(inp)
    assert out == actual, (out, actual)

    inp = 77
    out = True
    actual = Solution().isPalindrome(inp)
    assert out == actual, (out, actual)

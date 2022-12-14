"""
Given a non-negative integer num, return the number of steps to reduce it to zero.
If the current number is even, you have to divide it by 2, otherwise, you have to
subtract 1 from it.
"""
class Solution:
    def numberOfSteps (self, num: int) -> int:
        result = 0
        while num > 0:
            result += 1
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
        return result


if __name__ == "__main__":
    num = 14
    out = 6
    actual = Solution().numberOfSteps(num)
    assert actual == out, (actual, out)

    num = 8
    out = 4
    actual = Solution().numberOfSteps(num)
    assert actual == out, (actual, out)

    num = 123
    out = 12
    actual = Solution().numberOfSteps(num)
    assert actual == out, (actual, out)

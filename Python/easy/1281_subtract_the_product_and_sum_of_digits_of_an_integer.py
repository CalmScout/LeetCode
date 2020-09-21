"""
Given an integer number n, return the difference between the product of its digits and the sum of its digits.
"""
from functools import reduce


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = [int(x) for x in str(n)]
        prod = reduce((lambda x, y: x * y), digits)
        return prod - sum(digits)


if __name__ == "__main__":
    n = 234
    out = 15
    res = Solution().subtractProductAndSum(n)
    assert res == out, (res, out)

    n = 4421
    out = 21
    res = Solution().subtractProductAndSum(n)
    assert res == out, (res, out)

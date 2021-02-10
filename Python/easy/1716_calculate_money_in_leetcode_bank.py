"""
Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.
He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he
will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more
than the previous Monday. Given n, return the total amount of money he will have in the
Leetcode bank at the end of the nth day.

Constraints:
    * 1 <= n <= 1000
"""
class Solution:
    def totalMoney(self, n: int) -> int:
        k = n // 7
        p = n % 7
        result = 0
        for a1 in range(1, k + 1):
            result += (2 * a1 + 7 - 1) * 7 / 2
        a1 = k + 1
        result += (2 * a1 + p - 1) * p / 2
        return int(result)


if __name__ == "__main__":
    n = 4
    out = 10
    res = Solution().totalMoney(n)
    assert out == res, (out, res)

    n = 10
    out = 37
    res = Solution().totalMoney(n)
    assert out == res, (out, res)

    n = 20
    out = 96
    res = Solution().totalMoney(n)
    assert out == res, (out, res)
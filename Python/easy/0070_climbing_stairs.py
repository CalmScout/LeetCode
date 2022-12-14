"""
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct
ways can you climb to the top?
Note: Given n will be a positive integer.
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, len(dp)):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]


if __name__ == "__main__":
    n = 2
    out = 2
    actual = Solution().climbStairs(n)
    assert actual == out, (actual, out)

    n = 3
    out = 3
    actual = Solution().climbStairs(n)
    assert actual == out, (actual, out)

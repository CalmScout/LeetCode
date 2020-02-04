"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).

Example 1:
Input: 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:
Input: 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

Example 3:
Input: 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

Note:
0 ≤ N ≤ 30.
"""
class Solution:
    def fib(self, N: int) -> int:
        self.cache = {0: 0, 1: 1}
        for i in range(2, N+1):
            self.cache[i] = self.cache[i-1] + self.cache[i-2]
        return self.cache[N]


if __name__ == "__main__":
    assert Solution().fib(2) == 1, (Solution().fib(2), 1)
    assert Solution().fib(3) == 2, (Solution().fib(3), 2)
    assert Solution().fib(4) == 3, (Solution().fib(3), 3)

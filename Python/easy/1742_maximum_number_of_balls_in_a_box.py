"""
You are working in a ball factory where you have n balls numbered from lowLimit
up to highLimit inclusive (i.e., n == highLimit - lowLimit + 1), and an infinite
number of boxes numbered from 1 to infinity. Your job at this factory is to put
each ball in the box with a number equal to the sum of digits of the ball's number.
For example, the ball number 321 will be put in the box number 3 + 2 + 1 = 6 and
the ball number 10 will be put in the box number 1 + 0 = 1. Given two integers
lowLimit and highLimit, return the number of balls in the box with the most balls.

Constraints:
    * 1 <= lowLimit <= highLimit <= 105
"""
from collections import Counter


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        
        def get_digits_sum(n:int) -> int:
            s = str(n)
            lst = list(map(int, s.strip()))
            return sum(lst)
        
        arr = [get_digits_sum(el) for el in range(lowLimit, highLimit + 1)]
        c = Counter(arr)
        return max(c.values())


if __name__ == "__main__":
    lowLimit = 1
    highLimit = 10
    out = 2
    res = Solution().countBalls(lowLimit, highLimit)
    assert out == res, (out, res)

    lowLimit = 5
    highLimit = 15
    out = 2
    res = Solution().countBalls(lowLimit, highLimit)
    assert out == res, (out, res)

    lowLimit = 19
    highLimit = 28
    out = 2
    res = Solution().countBalls(lowLimit, highLimit)
    assert out == res, (out, res)

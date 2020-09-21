"""
Implement pow(x, n), which calculates x raised to the power n (xn).

Note:
    * -100.0 < x < 100.0
    * n is a 32-bit signed integer, within the range [−2^31, 2^31 − 1]
"""
import math


class Solution:
    
    def power(self, x,n):
        """Divide and conquer approach"""
        if n==0:
            return 1
        if n==1:
            return x
        a = self.power(x, n//2)
        if n%2==1:
            return x*a*a
        else:
            return a*a
        
        
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            return 1/self.power(x,-n)
        return self.power(x,n)


if __name__ == "__main__":
    x = 2.00000
    n = 10
    out = 1024.00000
    result = Solution().myPow(x, n)
    assert math.isclose(result, out, abs_tol=1e-4), (result, out)

    x = 2.10000
    n = 3
    out = 9.26100
    result = Solution().myPow(x, n)
    assert math.isclose(result, out, abs_tol=1e-4), (result, out)

    x = 2.00000
    n = -2
    out = 0.25000
    result = Solution().myPow(x, n)
    assert math.isclose(result, out, abs_tol=1e-4), (result, out)

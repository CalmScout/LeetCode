"""
Given an integer n, return any array containing n unique integers such that they add up to 0.
"""
from typing import List
import numpy as np


class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = [0 for _ in range(n)]
        val = 1
        if n % 2 == 1:
            result[n // 2] = 0
            for idx in range(1, n // 2 + 1):
                result[n // 2 - idx] = -val
                result[n // 2 + idx] = val
                val += 1
        else:
            right = n // 2
            left = right - 1
            while right < n:
                result[right] = val
                result[left] = -val
                right += 1
                left -= 1
                val += 1
        return result


if __name__ == "__main__":
    
    def check(n:int, arr: List[int]) -> bool:
        if np.sum(arr) == 0 and len(np.unique(arr)) == n:
            return True
        return False
    
    actual = Solution().sumZero(5)
    assert check(5, actual) == True, actual

    actual = Solution().sumZero(4)
    assert check(4, actual) == True, actual

    actual = Solution().sumZero(3)
    assert check(3, actual) == True, actual

    actual = Solution().sumZero(2)
    assert check(2, actual) == True, actual

    actual = Solution().sumZero(1)
    assert check(1, actual) == True, actual

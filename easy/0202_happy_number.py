"""
Write an algorithm to determine if a number is "happy".
A happy number is a number defined by the following process: Starting with any positive integer,
replace the number by the sum of the squares of its digits, and repeat the process until the
number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers.

Example:
Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""
class Solution:
    def isHappy(self, n: int) -> bool:
        nums = []
        def next(t:int) -> int:
            result = 0
            while t > 0:
                result += (t % 10) * (t % 10)
                t //= 10
            return result
        curr = n
        while curr != 1:
            if curr in nums:
                return False
            nums.append(curr)
            curr = next(curr)
        return True


if __name__ == "__main__":
    inp = 19
    out = True
    actual = Solution().isHappy(inp)
    assert actual == out, (actual, out)

    inp = 2
    out = False
    actual = Solution().isHappy(inp)
    assert actual == out, (actual, out)

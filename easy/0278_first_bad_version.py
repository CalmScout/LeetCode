"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality
check. Since each version is developed based on the previous version, all the versions after a bad version are also bad. Suppose you have n versions
[1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad. You are given an API
bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize
the number of calls to the API.

Example:

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version.
"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Data:
    def __init__(self, n, bad):
        assert bad <= n
        self.arr = [False] * (bad - 1) + [True] * (n - bad + 1)
    
    def isBadVersion(self, n):
        return self.arr[n-1]


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left <= right:
            middle = left + (right - left) // 2
            if isBadVersion(middle):
                right = middle - 1
            else:
                left = middle + 1
        return left


if __name__ == "__main__":
    d = Data(5, 3)
    isBadVersion = d.isBadVersion
    assert Solution().firstBadVersion(5) == 3

    d = Data(10, 10)
    isBadVersion = d.isBadVersion
    assert Solution().firstBadVersion(10) == 10

    d = Data(1, 1)
    isBadVersion = d.isBadVersion
    assert Solution().firstBadVersion(1) == 1

    d = Data(3, 1)
    isBadVersion = d.isBadVersion
    assert Solution().firstBadVersion(3) == 1

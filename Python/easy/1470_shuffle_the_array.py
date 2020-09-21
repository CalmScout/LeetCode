"""
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
Return the array in the form [x1,y1,x2,y2,...,xn,yn].
"""
from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i = 0
        res = []
        for _ in range(n):
            res.append(nums[i])
            res.append(nums[i + n])
            i += 1
        return res


if __name__ == "__main__":
    nums = [2, 5, 1, 3, 4, 7]
    n = 3
    out = [2, 3, 5, 4, 1, 7]
    s = Solution().shuffle(nums, n)
    assert s == out, (s, out)

    nums = [1, 2, 3, 4, 4, 3, 2, 1]
    n = 4
    out = [1, 4, 2, 3, 3, 2, 4, 1]
    s = Solution().shuffle(nums, n)
    assert s == out, (s, out)

    nums = [1, 1, 2, 2]
    n = 2
    out = [1, 2, 1, 2]
    s = Solution().shuffle(nums, n)
    assert s == out, (s, out)

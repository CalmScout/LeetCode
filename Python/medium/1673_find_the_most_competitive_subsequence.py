"""
Given an integer array nums and a positive integer k, return the most competitive subsequence of nums of size k.
An array's subsequence is a resulting sequence obtained by erasing some (possibly zero) elements from the array.
We define that a subsequence a is more competitive than a subsequence b (of the same length) if in the first position
where a and b differ, subsequence a has a number less than the corresponding number in b. For example, [1,3,4] is more
competitive than [1,3,5] because the first position they differ is at the final number, and 4 is less than 5.
"""
from typing import List


class Solution:
    def mostCompetitive(self, nums, k):
        attempts = len(nums) - k
        stack = []
        for num in nums:
            while stack and num < stack[-1] and attempts > 0:
                stack.pop()
                attempts -= 1
            stack.append(num)
        
        return stack[:k]


if __name__ == "__main__":
    nums = [3, 5, 2, 6]
    k = 2
    out = [2, 6]
    res = Solution().mostCompetitive(nums, k)
    assert out == res, (out, res)

    nums = [2, 4, 3, 3, 5, 4, 9, 6]
    k = 4
    out = [2, 3, 3, 4]
    res = Solution().mostCompetitive(nums, k)
    assert out == res, (out, res)


    nums = [71, 18, 52, 29, 55, 73, 24, 42, 66, 8, 80, 2]
    k = 3
    out = [8, 80, 2]
    res = Solution().mostCompetitive(nums, k)
    assert out == res, (out, res)

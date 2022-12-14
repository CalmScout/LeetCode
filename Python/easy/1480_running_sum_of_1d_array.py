"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.
"""
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        s = 0
        for el in nums:
            s += el
            result.append(s)
        return result


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    out = [1, 3, 6, 10]
    result = Solution().runningSum(nums)
    assert result == out, (result, out)


    nums = [1, 1, 1, 1, 1]
    out = [1, 2, 3, 4, 5]
    result = Solution().runningSum(nums)
    assert result == out, (result, out)

    nums = [3, 1, 2, 10, 1]
    out = [3, 4, 6, 16, 17]
    result = Solution().runningSum(nums)
    assert result == out, (result, out)

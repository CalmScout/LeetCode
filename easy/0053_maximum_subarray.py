"""
Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.
"""
class Solution:
    def maxSubArray(self, nums):
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i-1] + nums[i])
        return max(dp)


if __name__ == "__main__":
    inp = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    out = 6 # Explanation: [4,-1,2,1] has the largest sum = 6.
    actual = Solution().maxSubArray(inp)
    assert out == actual, (out, actual)

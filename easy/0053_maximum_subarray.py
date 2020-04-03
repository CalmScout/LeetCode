"""
Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.
"""
class Solution:
    def maxSubArray(self, nums):
        """
        Kadane's algorithm
        :type nums: List[int]
        :rtype: int
        """
        max_ending_here = max_so_far = nums[0]
        for el in nums[1:]:
            max_ending_here = max(max_ending_here + el, el)
            max_so_far = max(max_ending_here, max_so_far)
        return max_so_far



if __name__ == "__main__":
    inp = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    out = 6 # Explanation: [4,-1,2,1] has the largest sum = 6.
    actual = Solution().maxSubArray(inp)
    assert out == actual, (out, actual)

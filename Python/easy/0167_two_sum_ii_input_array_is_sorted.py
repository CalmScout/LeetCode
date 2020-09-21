"""
Given an array of integers that is already sorted in ascending order, find two numbers such that they
add up to a specific target number. The function twoSum should return indices of the two numbers such
that they add up to the target, where index1 must be less than index2.
Note:
Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
"""
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        x = {}
        for i in range(len(numbers)):
            t = target - numbers[i]
            if numbers[i] in x.keys():
                return [x[numbers[i]] + 1, i+1]
            else:
                x[t]=i


if __name__ == "__main__":
    numbers = [2, 7, 11, 15]
    target = 9
    out = [1, 2] # Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
    actual = Solution().twoSum(numbers, target)
    assert actual == out, (actual, out)

    numbers = [2, 3, 4]
    target = 6
    out = [1, 3] # Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
    actual = Solution().twoSum(numbers, target)
    assert actual == out, (actual, out)
"""
Given an array nums of integers, return how many of them contain an even number of digits.
 

Example 1:

Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.
Example 2:

Input: nums = [555,901,482,1771]
Output: 1 
Explanation: 
Only 1771 contains an even number of digits.
 

Constraints:

1 <= nums.length <= 500
1 <= nums[i] <= 10^5
"""
from typing import List
import math


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        counter = 0
        for el in nums:
            # int(math.log10(n))+1 - provides number of digits in the number
            if int(math.log10(el)) % 2 == 1:
                counter += 1
        return counter


if __name__ == "__main__":
    assert Solution().findNumbers([12, 345, 2, 6, 7896]) == 2
    assert Solution().findNumbers([555, 901, 482, 1771]) == 1
    assert Solution().findNumbers([]) == 0
    assert Solution().findNumbers([121]) == 0
    assert Solution().findNumbers([1234]) == 1
    assert Solution().findNumbers([22, 3333]) == 2

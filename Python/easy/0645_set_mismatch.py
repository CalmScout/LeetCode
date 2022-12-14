"""
The set S originally contains numbers from 1 to n. But unfortunately, due to the data error,
one of the numbers in the set got duplicated to another number in the set, which results in
repetition of one number and loss of another number. Given an array nums representing the
data status of this set after the error. Your task is to firstly find the number occurs twice
and then find the number that is missing. Return them in the form of an array.
"""
from typing import List
from collections import Counter


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        orig = set(range(1, len(nums) + 1))
        missed = orig.difference(set(nums)).pop()
        counter = Counter(nums)
        substitute = [el for el in counter if counter[el] == 2][0]
        return [substitute, missed]


if __name__ == "__main__":
    nums = [1, 2, 2, 4]
    out = [2, 3]
    res = Solution().findErrorNums(nums)
    assert res == out, (res, out)

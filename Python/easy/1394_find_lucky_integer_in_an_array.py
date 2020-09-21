"""
Given an array of integers arr, a lucky integer is an integer which has a frequency in the array equal to its value.
Return a lucky integer in the array. If there are multiple lucky integers return the largest of them. If there is no
lucky integer return -1.
"""
from typing import List
from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter = Counter(arr)
        result_lst = list(filter(lambda key: key == counter[key], counter))
        if result_lst:
            return max(result_lst)
        return -1


if __name__ == "__main__":
    arr = [2, 2, 3, 4]
    out = 2
    actual = Solution().findLucky(arr)
    assert actual == out, (actual, out)

    arr = [1, 2, 2, 3, 3, 3]
    out = 3
    actual = Solution().findLucky(arr)
    assert actual == out, (actual, out)

    arr = [2, 2, 2, 3, 3]
    out = -1
    actual = Solution().findLucky(arr)
    assert actual == out, (actual, out)

    arr = [5]
    out = -1
    actual = Solution().findLucky(arr)
    assert actual == out, (actual, out)

    arr = [7, 7, 7, 7, 7, 7, 7]
    out = 7
    actual = Solution().findLucky(arr)
    assert actual == out, (actual, out)

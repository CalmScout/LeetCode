"""
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  Elements
that don't appear in arr2 should be placed at the end of arr1 in ascending order.

 

Example 1:

Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]
 

Constraints:
arr1.length, arr2.length <= 1000
0 <= arr1[i], arr2[i] <= 1000
Each arr2[i] is distinct.
Each arr2[i] is in arr1.
"""
from typing import List
from collections import Counter


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = [None] * len(arr1)
        counter = Counter(arr1)
        idx_start = 0
        for key in arr2:
            idx_end = idx_start + counter[key]
            result[idx_start : idx_end] = [key] * counter[key]
            idx_start = idx_end
        rest = []
        for el in arr1:
            if not el in arr2:
                rest.append(el)
        result[idx_start:] = sorted(rest)
        return result


if __name__ == "__main__":
    arr1 = [2,3,1,3,2,4,6,7,9,2,19]
    arr2 = [2,1,4,3,9,6]
    output = [2,2,2,1,4,3,3,9,6,7,19]
    actual = Solution().relativeSortArray(arr1, arr2)
    assert actual == output, (actual, output)

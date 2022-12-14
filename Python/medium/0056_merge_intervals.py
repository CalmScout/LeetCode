"""
Given an array of intervals where intervals[i] = [starti, endi], merge all
overlapping intervals, and return an array of the non-overlapping intervals
that cover all the intervals in the input.
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        was_modified = True
        while was_modified:
            for i in range(len(intervals)):
                a0 = intervals[i][0]
                a1 = intervals[i][1]
                print(f"a0: {a0}, a1: {a1}")
                for j in range(i + 1, len(intervals)):
                    b0, b1 = intervals[j][0], intervals[j][1]
                    print(f"b0: {b0}, b1: {b1}")
                    if (b0 < a1 and a0 < b1) or (a0 < b1 and b0 < a1):
                        intervals.remove([a0, a1])
                        intervals.remove([b0, b1])
                        intervals.insert(min(a0, b0), max(a1, b1))
                        was_modified = True
                        break
        return intervals


if __name__ == "__main__":
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    out = [[1, 6], [8, 10], [15, 18]]
    res = Solution().merge(intervals)
    assert set(out) == set(res)

    intervals = [[1, 4], [4, 5]]
    out = [[1, 5]]
    res = Solution().merge(intervals)
    assert set(out) == set(res)

"""
Given two integer arrays startTime and endTime and given an integer queryTime.
The ith student started doing their homework at the time startTime[i] and finished
it at time endTime[i]. Return the number of students doing their homework at time
queryTime. More formally, return the number of students where queryTime lays in the
interval [startTime[i], endTime[i]] inclusive.
"""
from typing import List


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        result = 0
        for start, end in zip(startTime, endTime):
            if start <= queryTime and queryTime <= end:
                result += 1
        return result


if __name__ == "__main__":
    startTime = [1, 2, 3]
    endTime = [3, 2, 7]
    queryTime = 4
    out = 1
    res = Solution().busyStudent(startTime, endTime, queryTime)
    assert out == res, (out, res)

    startTime = [4]
    endTime = [4]
    queryTime = 4
    out = 1
    res = Solution().busyStudent(startTime, endTime, queryTime)
    assert out == res, (out, res)

    startTime = [4]
    endTime = [4]
    queryTime = 5
    out = 0
    res = Solution().busyStudent(startTime, endTime, queryTime)
    assert out == res, (out, res)

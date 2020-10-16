"""
On a plane there are n points with integer coordinates points[i] = [xi, yi]. Your task is to find the
minimum time in seconds to visit all points.
You can move according to the next rules:
 * In one second always you can either move vertically, horizontally by one unit or diagonally (it
   means to move one unit vertically and one unit horizontally in one second).
 * You have to visit the points in the same order as they appear in the array.
"""
from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        result = 0
        for i in range(len(points) - 1):
            dx = abs(points[i][0] - points[i+1][0])
            dy = abs(points[i][1] - points[i+1][1])
            result += max(dx, dy)
        return result


if __name__ == "__main__":
    points = [[1,1],[3,4],[-1,0]]
    out = 7
    res = Solution().minTimeToVisitAllPoints(points)
    assert res == out, (res, out)

    points = [[3,2],[-2,2]]
    out = 5
    res = Solution().minTimeToVisitAllPoints(points)
    assert res == out, (res, out)

    points = [[559,511],[932,618],[-623,-443],[431,91],[838,-127],[773,-917],[-500,-910],
    [830,-417],[-870,73],[-864,-600],[450,535],[-479,-370],[856,573],[-549,369],[529,-462],
    [-839,-856],[-515,-447],[652,197],[-83,345],[-69,423],[310,-737],[78,-201],[443,958],
    [-311,988],[-477,30],[-376,-153],[-272,451],[322,-125],[-114,-214],[495,33],[371,-533],
    [-393,-224],[-405,-633],[-693,297],[504,210],[-427,-231],[315,27],[991,322],[811,-746],
    [252,373],[-737,-867],[-137,130],[507,380],[100,-638],[-296,700],[341,671],[-944,982],
    [937,-440],[40,-929],[-334,60],[-722,-92],[-35,-852],[25,-495],[185,671],[149,-452]]
    out = 49088
    res = Solution().minTimeToVisitAllPoints(points)
    assert res == out, (res, out)

"""
You are given the array paths, where paths[i] = [cityAi, cityBi] means
there exists a direct path going from cityAi to cityBi. Return the destination
city, that is, the city without any path outgoing to another city.
It is guaranteed that the graph of paths forms a line without any loop, therefore,
there will be exactly one destination city.
"""
from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        s_to = set()
        s_from = set()
        for link in paths:
            s_from.add(link[0])
            s_to.add(link[1])
        return s_to.difference(s_from).pop()


if __name__ == "__main__":
    paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
    out = "Sao Paulo"
    res = Solution().destCity(paths)
    assert res == out, (res, out)

    paths = [["B","C"],["D","B"],["C","A"]]
    out = "A"
    res = Solution().destCity(paths)
    assert res == out, (res, out)

    paths = [["A", "Z"]]
    out = "Z"
    res = Solution().destCity(paths)
    assert res == out, (res, out)

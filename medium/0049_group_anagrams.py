"""
Given an array of strings, group anagrams together.

Note:
All inputs will be in lowercase.
The order of your output does not matter.
"""
from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for el in strs:
            key = ''.join(sorted(el))
            d[key].append(el)
        return list(d.values())


if __name__ == "__main__":
    def sort_items_(lst:List[List[str]]) -> List[List[str]]:
        for i in range(len(lst)):
            lst[i] = sorted(lst[i])
        return sorted(lst)
    
    inp = ["eat", "tea", "tan", "ate", "nat", "bat"]
    out = [
        ["ate", "eat", "tea"],
        ["bat"],
        ["nat", "tan"]
    ]
    assert sort_items_(Solution().groupAnagrams(inp)) == out

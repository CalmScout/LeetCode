"""
Given an array A of strings made only from lowercase letters, return a list of
all characters that show up in all strings within the list (including duplicates). 
For example, if a character occurs 3 times in all strings but not 4 times, you
need to include that character three times in the final answer.
You may return the answer in any order.
"""
from typing import List
from collections import Counter


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        res = Counter([ch for ch in A[0]])
        # build intersection of all Counters
        for s in A[1:]:
            candidate = Counter([x for x in s])
            res = {key: min(res[key], candidate[key]) for key in res if key in candidate}
        # convert resulting counter into the list
        final_res = []
        for key in res:
            for _ in range(res[key]):
                final_res.append(key)
        return final_res


if __name__ == "__main__":
    inp = ["bella", "label", "roller"]
    out = ["e", "l", "l"]
    res = Counter(Solution().commonChars(inp))
    assert res == Counter(out)

    inp = ["cool", "lock", "cook"]
    out = ["c", "o"]
    res = Counter(Solution().commonChars(inp))
    assert res == Counter(out)

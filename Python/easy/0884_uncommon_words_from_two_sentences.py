"""
We are given two sentences A and B.  (A sentence is a string of space separated words. 
Each word consists only of lowercase letters.) A word is uncommon if it appears exactly
once in one of the sentences, and does not appear in the other sentence. Return a list
of all uncommon words. You may return the list in any order.
"""
from typing import List
from collections import Counter


class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        tmp = A.split()
        tmp.extend(B.split())
        c = Counter(tmp)
        res = [el for el in c if c[el] == 1]
        return res


if __name__ == "__main__":
    A = "this apple is sweet"
    B = "this apple is sour"
    out = ["sweet","sour"]
    res = Solution().uncommonFromSentences(A, B)
    assert set(res) == set(out) and len(res) == len(out)

    A = "apple apple"
    B = "banana"
    out = ["banana"]
    res = Solution().uncommonFromSentences(A, B)
    assert set(res) == set(out) and len(res) == len(out)

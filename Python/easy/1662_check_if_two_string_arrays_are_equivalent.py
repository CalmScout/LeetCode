"""
Given two string arrays word1 and word2, return true if the two arrays represent the same string,
and false otherwise. A string is represented by an array if the array elements concatenated in
order forms the string.
"""
from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # check lengths first and return False in the case
        # of different lengths
        len_1, len_2 = 0, 0
        for w in word1: len_1 += len(w)
        for w in word2: len_2 += len(w)
        if len_1 != len_2: return False

        # in the case of equal lengths check if corresponding
        # characters are equal
        def next_char(arr):
            for word in arr:
                for c in word:
                    yield c
        iter_1 = iter(next_char(word1))
        iter_2 = iter(next_char(word2))

        for ch_1, ch_2 in zip(iter_1, iter_2):
            if ch_1 != ch_2:
                return False
        
        return True


if __name__ == "__main__":
    word1 = ["ab", "c"]
    word2 = ["a", "bc"]
    out = True
    res = Solution().arrayStringsAreEqual(word1, word2)
    assert res == out, (res, out)

    word1 = ["a", "cb"]
    word2 = ["ab", "c"]
    out = False
    res = Solution().arrayStringsAreEqual(word1, word2)
    assert res == out, (res, out)

    word1  = ["abc", "d", "defg"]
    word2 = ["abcddefg"]
    out = True
    res = Solution().arrayStringsAreEqual(word1, word2)
    assert res == out, (res, out)

    word1 = ["abc", "d", "defg"]
    word2 = ["abcddef"]
    out = False
    res = Solution().arrayStringsAreEqual(word1, word2)
    assert res == out, (res, out)

"""
Two strings are considered close if you can attain one from the other using the following operations:
Operation 1: Swap any two existing characters.
    * For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
    * For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.
Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

Constraints:
    * 1 <= word1.length, word2.length <= 105
    * word1 and word2 contain only lowercase English letters.
"""
from collections import Counter


class Solution:
    def closeStrings(self, w1, w2):
        return set(w1) == set(w2) and Counter(Counter(w1).values()) == Counter(Counter(w2).values())
        


if __name__ == "__main__":
    word1 = "abc"
    word2 = "bca"
    out = True
    res = Solution().closeStrings(word1, word2)
    assert out == res, (out, res)

    word1 = "a"
    word2 = "aa"
    out = False
    res = Solution().closeStrings(word1, word2)
    assert out == res, (out, res)

    word1 = "cabbba"
    word2 = "abbccc"
    out = True
    res = Solution().closeStrings(word1, word2)
    assert out == res, (out, res)

    word1 = "cabbba"
    word2 = "aabbss"
    out = False
    res = Solution().closeStrings(word1, word2)
    assert out == res, (out, res)

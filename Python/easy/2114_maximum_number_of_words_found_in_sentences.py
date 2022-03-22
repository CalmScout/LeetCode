"""
A sentence is a list of words that are separated by a single space with
no leading or trailing spaces. You are given an array of strings sentences,
where each sentences[i] represents a single sentence. Return the maximum
number of words that appear in a single sentence.
"""
from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        res = 0
        for word in sentences:
            candidate = 0
            for char in word:
                if char == " ":
                    candidate += 1
            candidate += 1
            res = max(res, candidate)
        return res


if __name__ == "__main__":
    sentences = ["alice and bob love leetcode",
                 "i think so too",
                 "this is great thanks very much"]
    out = 6
    res = Solution().mostWordsFound(sentences)
    assert res == out, res

    sentences = ["please wait",
                 "continue to fight",
                 "continue to win"]
    out = 3
    res = Solution().mostWordsFound(sentences)
    assert res == out, res

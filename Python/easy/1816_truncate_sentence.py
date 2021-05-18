"""
A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
Each of the words consists of only uppercase and lowercase English letters (no punctuation).
For example, "Hello World", "HELLO", and "hello world hello world" are all sentences.
You are given a sentence s​​​​​​ and an integer k​​​​​​. You want to truncate s​​​​​​ such that it contains only the first
k​​​​​​ words. Return s​​​​​​ after truncating it.
"""
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        lst = s.split()[:k]
        return " ".join(lst)


if __name__ == "__main__":
    s = "Hello how are you Contestant"
    k = 4
    out = "Hello how are you"
    res = Solution().truncateSentence(s, k)
    assert out == res, (out, res)

    s = "What is the solution to this problem"
    k = 4
    out = "What is the solution"
    res = Solution().truncateSentence(s, k)
    assert out == res, (out, res)

    s = "chopper is not a tanuki"
    k = 5
    out = "chopper is not a tanuki"
    res = Solution().truncateSentence(s, k)
    assert out == res, (out, res)

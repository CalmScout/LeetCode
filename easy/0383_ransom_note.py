"""
Given an arbitrary ransom note string and another string containing letters from all the magazines,
write a function that will return true if the ransom note can be constructed from the magazines;
otherwise, it will return false.
Each letter in the magazine string can only be used once in your ransom note.
"""
from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c_note = Counter(ransomNote)
        c_magazine = Counter(magazine)
        for key in c_note:
            if not key in c_magazine or c_note[key] > c_magazine[key]:
                return False
        return True


if __name__ == "__main__":
    ransomNote = "a"
    magazine = "b"
    out = False
    actual = Solution().canConstruct(ransomNote, magazine)
    assert out == actual, (out, actual)
    
    ransomNote = "aa"
    magazine = "ab"
    out = False
    actual = Solution().canConstruct(ransomNote, magazine)
    assert out == actual, (out, actual)

    ransomNote = "aa"
    magazine = "aab"
    out = True
    actual = Solution().canConstruct(ransomNote, magazine)
    assert out == actual, (out, actual)

    ransomNote = "aab"
    magazine = "baa"
    out = True
    actual = Solution().canConstruct(ransomNote, magazine)
    assert out == actual, (out, actual)

"""
You are given an array of strings words and a string chars.
A string is good if it can be formed by characters from chars
(each character can only be used once).
Return the sum of lengths of all good strings in words.

Example 1:
Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: 
The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

Example 2:
Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: 
The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.

Note:
1 <= words.length <= 1000
1 <= words[i].length, chars.length <= 100
All strings contain lowercase English letters only.
"""
from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        def can_construct(word: str, chars: str) -> bool:
            for letter in word:
                if word.count(letter) > chars.count(letter):
                    return False
            return True
        
        result = 0
        for word in words:
            if can_construct(word, chars):
                result += len(word)
        
        return result


if __name__ == "__main__":
    words = ["cat", "bt", "hat", "tree"]
    chars = "atach"
    actual = Solution().countCharacters(words, chars)
    assert  actual == 6, (f"f({words}, {chars}) == {actual}, needed {6}")
    assert Solution().countCharacters(words=["hello", "world", "leetcode"], chars="welldonehoneyr") == 10

"""
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different
order. The order of the alphabet is some permutation of lowercase letters. Given a sequence of words
written in the alien language, and the order of the alphabet, return true if and only if the given words
are sorted lexicographicaly in this alien language.

Example 1:
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:
Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is
unsorted.

Example 3:
Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According
to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character
which is less than any other character (More info). 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.
"""
from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_index = {c: i for i, c in enumerate(order)}

        for i in range(len(words) - 1):
            word_1 = words[i]
            word_2 = words[i+1]
            
            # find first different symbol
            for idx in range(min(len(word_1), len(word_2))):
                # if two neighbour words not sorted - all sequence
                # is not sorted
                if word_1[idx] != word_2[idx]:
                    if order_index[word_1[idx]] > order_index[word_2[idx]]:
                        return False
                    break
                else:
                    if len(word_1) > len(word_2):
                        return False
        return True


if __name__ == "__main__":
    words = ["hello", "leetcode"]
    order = "hlabcdefgijkmnopqrstuvwxyz"
    assert Solution().isAlienSorted(words, order) == True

    words = ["word", "world", "row"]
    order = "worldabcefghijkmnpqstuvxyz"
    assert Solution().isAlienSorted(words, order) == False

    words = ["apple","app"]
    order = "abcdefghijklmnopqrstuvwxyz"
    assert Solution().isAlienSorted(words, order) == False

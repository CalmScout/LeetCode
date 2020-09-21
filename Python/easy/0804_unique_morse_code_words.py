"""
International Morse Code defines a standard encoding where each letter is mapped to a series of dots and
dashes, as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on. For convenience,
the full table for the 26 letters of the English alphabet is given below: [".-","-...","-.-.","-..",".",
"..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",
".--","-..-","-.--","--.."]
Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter.
For example, "cab" can be written as "-.-..--...", (which is the concatenation "-.-." + ".-" + "-...").
We'll call such a concatenation, the transformation of a word. Return the number of different
transformations among all words we have.
"""
from typing import List
import string


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        alphabet = list(string.ascii_lowercase)
        codes = [".-","-...","-.-.","-..",".","..-.","--.","....",
        "..",".---","-.-",".-..","--","-.","---",".--.","--.-",
        ".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        d = {}
        for idx, c in enumerate(alphabet):
            d[c] = codes[idx]
        uniques = set()
        for word in words:
            encoding = []
            for ch in word:
                encoding.append(d[ch])
            uniques.add("".join(encoding))
        return len(uniques)


if __name__ == "__main__":
    words = ["gin", "zen", "gig", "msg"]
    out = 2
    res = Solution().uniqueMorseRepresentations(words)
    assert res == out, (res, out)

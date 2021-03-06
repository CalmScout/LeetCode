"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that
the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1
does not map to any letters.
2 - abc
3 - def
4 - ghi
5 - jkl
6 - mno
7 - pqrs
8 - tuv
9 - wxyz

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
"""
from typing import List
from itertools import product


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        d = {
            1: "",
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }
        my_list = []
        for digit in digits:
            my_list.append(d[int(digit)])
        
        result = product(*my_list)

        res_lst = []
        for el in result:    
            res_lst.append("".join(el))
        
        return res_lst


if __name__ == "__main__":
    output = sorted(Solution().letterCombinations("23"))
    correct = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    assert output == correct, (output, correct)

    output = sorted(Solution().letterCombinations(""))
    correct = []
    assert output == correct, (output, correct)

"""
Given a string S, we can transform every letter individually to be lowercase or
uppercase to create another string. Return a list of all possible strings we could
create. You can return the output in any order.

Constraints:
    * S will be a string with length between 1 and 12.
    * S will consist only of letters or digits.
"""
from typing import List


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        arr = [char for char in S]
        # indexes of letters in the string
        alpha_idxs = []
        for idx, char in enumerate(S):
            if char.isalpha():
                alpha_idxs.append(idx)
        # create representation of lowercase/uppercase indexes
        n = len(alpha_idxs)
        lst = [bin(x)[2:].rjust(n, '0') for x in range(2**n)]
        # generate result
        result = []
        for pos in lst:
            tmp = []
            # index over `pos`
            idx_pos = 0
            for idx, ch in enumerate(arr):
                # if we see the letter check what version to add
                if idx in alpha_idxs:
                    if pos[idx_pos] == '1':
                        tmp.append(ch.upper())
                    else:
                        tmp.append(ch.lower())
                    idx_pos += 1
                # if we see the number just append it
                else:
                    tmp.append(ch)
            result.append(''.join(tmp))
        return result


if __name__ == "__main__":
    S = "a1b2"
    out = ["a1b2", "a1B2", "A1b2", "A1B2"]
    res = Solution().letterCasePermutation(S)
    assert set(out) == set(res)

    S = "3z4"
    out = ["3z4", "3Z4"]
    res = Solution().letterCasePermutation(S)
    assert set(out) == set(res)

    S = "12345"
    out = ["12345"]
    res = Solution().letterCasePermutation(S)
    assert set(out) == set(res)

    S = "0"
    out = ["0"]
    res = Solution().letterCasePermutation(S)
    assert set(out) == set(res)

    S = "C"
    out = ["c", "C"]
    res = Solution().letterCasePermutation(S)
    assert set(out) == set(res)

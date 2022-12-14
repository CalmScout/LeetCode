"""
You are given a large integer represented as an integer array digits,
where each digits[i] is the ith digit of the integer. The digits are
ordered from most significant to least significant in left-to-right
order. The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of
digits.
"""
from typing import List
import numpy as np


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = digits.copy()
        for idx in range(len(res)-1, -1, -1):
            if res[idx] == 9:
                res[idx] = 0
                # if the last digit we should increase the list
                if idx == 0:
                    res_extended = [1]
                    res_extended.extend(res)
                    return res_extended
            else:
                res[idx]  = res[idx] + 1
                return res


if __name__ == "__main__":
    digits = [1, 2, 3]
    out = [1, 2, 4]
    res = Solution().plusOne(digits)
    assert (np.array(out) == np.array(res)).all()

    digits = [4, 3, 2, 1]
    out = [4, 3, 2, 2]
    res = Solution().plusOne(digits)
    assert (np.array(out) == np.array(res)).all()

    digits = [9]
    out = [1, 0]
    res = Solution().plusOne(digits)
    assert (np.array(out) == np.array(res)).all()

    digits = [9, 9]
    out = [1, 0, 0]
    res = Solution().plusOne(digits)
    assert (np.array(out) == np.array(res)).all()

    digits = [9, 5, 9]
    out = [9, 6, 0]
    res = Solution().plusOne(digits)
    assert (np.array(out) == np.array(res)).all()

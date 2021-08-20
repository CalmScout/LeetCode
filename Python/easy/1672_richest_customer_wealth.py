"""
You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank.
Return the wealth that the richest customer has. A customer's wealth is the amount of money they have in all their bank
accounts. The richest customer is the customer that has the maximum wealth.
"""
from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        result = 0
        for client in accounts:
            curr = sum(client)
            if curr > result:
                result = curr
        return result


if __name__ == "__main__":
    accounts = [[1, 2, 3], [3, 2, 1]]
    out = 6
    res = Solution().maximumWealth(accounts)
    assert out == res, (out, res)

    accounts = [[1, 5], [7, 3], [3, 5]]
    out = 10
    res = Solution().maximumWealth(accounts)
    assert out == res, (out, res)

    accounts = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]
    out = 17
    res = Solution().maximumWealth(accounts)
    assert out == res, (out, res)

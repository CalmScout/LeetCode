"""
Given the array prices where prices[i] is the price of the ith item in a shop.
There is a special discount for items in the shop, if you buy the ith item, then
you will receive a discount equivalent to prices[j] where j is the minimum index
such that j > i and prices[j] <= prices[i], otherwise, you will not receive any
discount at all.
Return an array where the ith element is the final price you will pay for the ith
item of the shop considering the special discount.
"""
from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = []
        for i in range(len(prices) - 1):
            for j in range(i+1, len(prices)):
                sale = 0
                if prices[j] <= prices[i]:
                    sale = prices[j]
                    break
            res.append(prices[i] - sale)
        res.append(prices[-1])
        return res


if __name__ == "__main__":
    prices = [8, 4, 6, 2, 3]
    out = [4, 2, 4, 2, 3]
    res = Solution().finalPrices(prices)
    assert out == res, (out, res)

    prices = [1, 2, 3, 4, 5]
    out = [1, 2, 3, 4, 5]
    res = Solution().finalPrices(prices)
    assert out == res, (out, res)

    prices = [10, 1, 1, 6]
    out = [9, 0, 1, 6]
    res = Solution().finalPrices(prices)
    assert out == res, (out, res)

    prices = [8, 7, 4, 2, 8, 1, 7, 7, 10, 1]
    out = [1, 3, 2, 1, 7, 0, 0, 6, 9, 1]
    res = Solution().finalPrices(prices)
    assert out == res, (out, res)

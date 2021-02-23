"""
You have a long flowerbed in which some of the plots are planted, and some are not.
However, flowers cannot be planted in adjacent plots. Given an integer array flowerbed
containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n,
return if n new flowers can be planted in the flowerbed without violating the
no-adjacent-flowers rule.

Constraints:
    * 1 <= flowerbed.length <= 2 * 10^4
    * flowerbed[i] is 0 or 1.
    * There are no two adjacent flowers in flowerbed.
    * 0 <= n <= flowerbed.length
"""
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if flowerbed == [0]: return n <= 1
        if flowerbed == [1]: return False
        remains_to_plant = n
        new_flowerbed = [el for el in flowerbed]
        for idx in range(len(flowerbed)):
            if remains_to_plant == 0:
                break
            # check separetly the first element
            if idx == 0:
                if new_flowerbed[idx] == 0 and new_flowerbed[idx + 1] == 0:
                    remains_to_plant -= 1
                    new_flowerbed[idx] = 1
            # check separately the last element
            elif idx == len(new_flowerbed) - 1:
                if new_flowerbed[idx] == 0 and new_flowerbed[idx - 1] == 0:
                    remains_to_plant -= 1
                    new_flowerbed[idx] = 1
            # no corner cases
            else:
                if new_flowerbed[idx - 1] == 0 and new_flowerbed[idx] == 0 and new_flowerbed[idx + 1] == 0:
                    remains_to_plant -= 1
                    new_flowerbed[idx] = 1
        return remains_to_plant == 0


if __name__ == "__main__":
    flowerbed = [1, 0, 0, 0, 1]
    n = 1
    out = True
    res = Solution().canPlaceFlowers(flowerbed=flowerbed, n=n)
    assert res == out, (res, out)

    flowerbed = [1, 0, 0, 0, 1]
    n = 2
    out = False
    res = Solution().canPlaceFlowers(flowerbed=flowerbed, n=n)
    assert res == out, (res, out)

    flowerbed = [1,0,0,0,0,1]
    n = 2
    out = False
    res = Solution().canPlaceFlowers(flowerbed=flowerbed, n=n)
    assert res == out, (res, out)

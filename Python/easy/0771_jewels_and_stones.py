"""
You're given strings J representing the types of stones that are jewels, and S representing
the stones you have.  Each character in S is a type of stone you have.  You want to know how
many of the stones you have are also jewels. The letters in J are guaranteed distinct, and
all characters in J and S are letters. Letters are case sensitive, so "a" is considered a
different type of stone from "A".
"""
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        result = 0
        for stone in S:
            if stone in J:
                result += 1
        return result


if __name__ == "__main__":
    J = "aA"
    S = "aAAbbbb"
    out = 3
    actual = Solution().numJewelsInStones(J, S)
    assert  actual == out, (actual, out)

    J = "z"
    S = "ZZ"
    out = 0
    actual = Solution().numJewelsInStones(J, S)
    assert  actual == out, (actual, out)

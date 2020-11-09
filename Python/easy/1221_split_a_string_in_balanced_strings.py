"""
Balanced strings are those who have equal quantity of 'L' and 'R' characters.
Given a balanced string s split it in the maximum amount of balanced strings.
Return the maximum amount of splitted balanced strings.
"""
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        x = 0
        split_count = 0
        for char in s:
            if char == 'R':
                x += 1
            else:
                x -= 1
            
            if x == 0:
                split_count += 1
        
        return split_count


if __name__ == "__main__":
    s = "RLRRLLRLRL"
    out = 4
    res = Solution().balancedStringSplit(s)
    assert res == out, (res, out)

    s = "RLLLLRRRLR"
    out = 3
    res = Solution().balancedStringSplit(s)
    assert res == out, (res, out)

    s = "LLLLRRRR"
    out = 1
    res = Solution().balancedStringSplit(s)
    assert res == out, (res, out)

    s = "RLRRRLLRLL"
    out = 2
    res = Solution().balancedStringSplit(s)
    assert res == out, (res, out)

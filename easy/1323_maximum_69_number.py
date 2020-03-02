"""
Given a positive integer num consisting only of digits 6 and 9.
Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).
"""
class Solution:
    def maximum69Number (self, num: int) -> int:
        num_str = str(num)
        result = num
        for idx, el in enumerate(num_str):
            if el == "6":
                result = int(num_str[:idx] + "9" + num_str[idx+1:])
                break
        return result


if __name__ == "__main__":
    inp = 9669
    out = 9969
    actual = Solution().maximum69Number(inp)
    assert out == actual, (out, actual)

    inp = 9996
    out = 9999
    actual = Solution().maximum69Number(inp)
    assert out == actual, (out, actual)

    inp = 9999
    out = 9999
    actual = Solution().maximum69Number(inp)
    assert out == actual, (out, actual)

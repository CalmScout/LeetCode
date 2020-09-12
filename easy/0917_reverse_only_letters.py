"""
Given a string S, return the "reversed" string where all characters that are not a
letter stay in the same place, and all letters reverse their positions.
"""
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        tmp = []
        for ch in S:
            if ch.isalpha():
                tmp.append(ch)
        res = []
        it = iter(tmp[::-1])
        for el in S:
            if el.isalpha():
                res.append(next(it))
            else:
                res.append(el)
        return ''.join(res)


if __name__ == "__main__":
    inp = "ab-cd"
    out = "dc-ba"
    res = Solution().reverseOnlyLetters(inp)
    assert res == out, (res, out)

    inp = "a-bC-dEf-ghIj"
    out = "j-Ih-gfE-dCba"
    res = Solution().reverseOnlyLetters(inp)
    assert res == out, (res, out)

    inp = "Test1ng-Leet=code-Q!"
    out = "Qedo1ct-eeLg=ntse-T!"
    res = Solution().reverseOnlyLetters(inp)
    assert res == out, (res, out)

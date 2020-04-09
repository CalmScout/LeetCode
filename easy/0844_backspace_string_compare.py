"""
Given two strings S and T, return if they are equal when both are typed
into empty text editors. # means a backspace character.
Note:
1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
"""
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def fill_stack(s:str):
            result = []
            for el in s:
                if not el == '#':
                    result.append(el)
                elif len(result) > 0:
                    result.pop()
            return result
        
        s_stack = fill_stack(S)
        t_stack = fill_stack(T)
        return s_stack == t_stack


if __name__ == "__main__":
    S = "ab#c"
    T = "ad#c"
    out = True
    actual = Solution().backspaceCompare(S, T)
    assert actual == out, (actual, out)

    S = "ab##"
    T = "c#d#"
    out = True
    actual = Solution().backspaceCompare(S, T)
    assert actual == out, (actual, out)

    S = "a##c"
    T = "#a#c"
    out = True
    actual = Solution().backspaceCompare(S, T)
    assert actual == out, (actual, out)

    S = "a#c"
    T = "b"
    out = False
    actual = Solution().backspaceCompare(S, T)
    assert actual == out, (actual, out)

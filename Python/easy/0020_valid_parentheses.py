"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.
An input string is valid if:
* Open brackets must be closed by the same type of brackets.
* Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        right2left = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for el in s:
            if el in right2left.values():
                stack.append(el)
            elif el in right2left.keys():
                if not stack:
                    return False
                if stack.pop() != right2left[el]:
                    return False
            else:
                return False
        return len(stack) == 0


if __name__ == "__main__":
    s = "()"
    out = True
    actual = Solution().isValid(s)
    assert actual == out, (actual, out)

    s = "()[]{}"
    out = True
    actual = Solution().isValid(s)
    assert actual == out, (actual, out)

    s = "(]"
    out = False
    actual = Solution().isValid(s)
    assert actual == out, (actual, out)

    s = "([)]"
    out = False
    actual = Solution().isValid(s)
    assert actual == out, (actual, out)

    s = "["
    out = False
    actual = Solution().isValid(s)
    assert actual == out, (actual, out)

    s = "}"
    out = False
    actual = Solution().isValid(s)
    assert actual == out, (actual, out)
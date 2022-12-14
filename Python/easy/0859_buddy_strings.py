"""
Given two strings A and B of lowercase letters, return true if and only if we can
swap two letters in A so that the result equals B.
"""
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        elif A == B:
            return len(set(A)) < len(A)
        result = True
        swapped = False
        a_first, b_first = None, None
        for a, b in zip(A, B):
            if a != b:
                if swapped:
                    return False
                if a_first is None:
                    a_first = a
                    b_first = b
                else:
                    if a_first != b or b_first != a:
                        return False
                    else:
                        swapped = True
        return result


if __name__ == "__main__":
    A = "ab"
    B = "ba"
    assert Solution().buddyStrings(A, B) == True

    A = "ab"
    B = "ab"
    assert Solution().buddyStrings(A, B) == False

    A = "aa"
    B = "aa"
    assert Solution().buddyStrings(A, B) == True

    A = "aaaaaaabc"
    B = "aaaaaaacb"
    assert Solution().buddyStrings(A, B) == True

    A = ""
    B = "aa"
    assert Solution().buddyStrings(A, B) == False

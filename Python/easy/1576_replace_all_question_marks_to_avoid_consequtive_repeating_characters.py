"""
Given a string s containing only lower case English letters and the '?' character,
convert all the '?' characters into lower case letters such that the final string
does not contain any consecutive repeating characters. You cannot modify the non
'?' characters. It is guaranteed that there are no consecutive repeating characters
in the given string except for '?'. Return the final string after all the conversions
(possibly zero) have been made. If there is more than one solution, return any of
them. It can be shown that an answer is always possible with the given constraints.
"""
class Solution:
    def modifyString(self, s: str) -> str:
        if s == '?':
            return 'a'
        alphabet = set("abcdefghijklmnopqrstuvwxyz")
        result = ""
        for idx in range(len(s)):
            if s[idx] != '?':
                result += s[idx]
            else:
                if idx == 0:
                    for el in alphabet:
                        if el != s[1]:
                            result += el
                            break
                elif idx == len(s) - 1:
                    for el in alphabet:
                        if el != s[len(s) - 2]:
                            result += el
                            break
                else:
                    for el in alphabet:
                        if el != s[idx-1] and el != s[idx+1]:
                            result += el
                            break
        return result

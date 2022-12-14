"""
You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G",
"()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string
"o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.
Given the string command, return the Goal Parser's interpretation of command.

Constraints:
    * 1 <= command.length <= 100
    * command consists of "G", "()", and/or "(al)" in some order.
"""
class Solution:
    def interpret(self, command: str) -> str:
        res = command
        res = res.replace("()", "o")
        res = res.replace("(al)", "al")
        return res


if __name__ == "__main__":
    command = "G()(al)"
    out = "Goal"
    res = Solution().interpret(command)
    assert out == res, (out, res)

    command = "G()()()()(al)"
    out = "Gooooal"
    res = Solution().interpret(command)
    assert out == res, (out, res)

    command = "(al)G(al)()()G"
    out = "alGalooG"
    res = Solution().interpret(command)
    assert out == res, (out, res)

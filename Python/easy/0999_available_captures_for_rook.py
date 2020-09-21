"""
On an 8 x 8 chessboard, there is one white rook.  There also may be empty squares, white bishops,
and black pawns.  These are given as characters 'R', '.', 'B', and 'p' respectively. Uppercase
characters represent white pieces, and lowercase characters represent black pieces. The rook moves
as in the rules of Chess: it chooses one of four cardinal directions (north, east, west, and south),
then moves in that direction until it chooses to stop, reaches the edge of the board, or captures an
opposite colored pawn by moving to the same square it occupies.  Also, rooks cannot move into the
same square as other friendly bishops.
Return the number of pawns the rook can capture in one move.

Example 1
Input: [[".",".",".",".",".",".",".","."],
        [".",".",".","p",".",".",".","."],
        [".",".",".","R",".",".",".","p"],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".","p",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."]]
Output: 3
Explanation: 
In this example the rook is able to capture all the pawns.

Example 2
Input: [[".",".",".",".",".",".",".","."],
        [".","p","p","p","p","p",".","."],
        [".","p","p","B","p","p",".","."],
        [".","p","B","R","B","p",".","."],
        [".","p","p","B","p","p",".","."],
        [".","p","p","p","p","p",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."]]
Output: 0
Explanation: 
Bishops are blocking the rook to capture any pawn.

Example 3
Input: [[".",".",".",".",".",".",".","."],
        [".",".",".","p",".",".",".","."],
        [".",".",".","p",".",".",".","."],
        ["p","p",".","R",".","p","B","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".","B",".",".",".","."],
        [".",".",".","p",".",".",".","."],
        [".",".",".",".",".",".",".","."]]
Output: 3
Explanation: 
The rook can capture the pawns at positions b5, d6 and f5.
"""
from typing import List


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        # detect all figures
        i_rook, j_rook = None, None
        B = []
        p = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                el = board[i][j]
                if el != ".":
                    if el == "p":
                        p.append((i, j))
                    elif el == "B":
                        B.append((i, j))
                    else:
                        i_rook = i
                        j_rook = j
        result = 0
        # detect LEFT
        left_candidates_p = sorted([el[1] for el in p if el[0] == i_rook and el[1] < j_rook], reverse=True)
        left_candidates_B = sorted([el[1] for el in B if el[0] == i_rook and el[1] < j_rook], reverse=True)
        if len(left_candidates_p) > 0 and len(left_candidates_B) == 0:
            result += 1
        elif len(left_candidates_p) > 0 and len(left_candidates_B) > 0:
            if left_candidates_p[0] > left_candidates_B[0]:
                result += 1
        # detect RIGHT
        right_candidates_p = sorted([el[1] for el in p if el[0] == i_rook and el[1] > j_rook])
        right_candidates_B = sorted([el[1] for el in B if el[0] == i_rook and el[1] > j_rook])
        if len(right_candidates_p) != 0 and len(right_candidates_B) == 0:
            result +=1
        elif len(right_candidates_p) > 0 and len(right_candidates_B) > 0:
            if right_candidates_p[0] < right_candidates_B[0]:
                result += 1
        # detect UP
        up_candidates_p = sorted([el[0] for el in p if el[1] == j_rook and el[0] < i_rook], reverse=True)
        up_candidates_B = sorted([el[0] for el in B if el[1] == j_rook and el[0] < i_rook], reverse=True)
        if len(up_candidates_p) > 0 and len(up_candidates_B) == 0:
            result += 1
        elif len(up_candidates_p) > 0 and len(up_candidates_B) > 0:
            if up_candidates_p[0] > up_candidates_B[0]:
                result += 1
        # detect DOWN
        down_candidates_p = sorted([el[0] for el in p if el[1] == j_rook and el[0] > i_rook])
        down_candidates_B = sorted([el[0] for el in B if el[1] == j_rook and el[0] > i_rook])
        if len(down_candidates_p) > 0 and len(down_candidates_B) == 0:
            result += 1
        elif len(down_candidates_p) > 0 and len(down_candidates_B) > 0:
            if down_candidates_p[0] < down_candidates_B[0]:
                result += 1
        return result


if __name__ == "__main__":
    inp = [[".",".",".",".",".",".",".","."],
           [".",".",".","p",".",".",".","."],
           [".",".",".","R",".",".",".","p"],
           [".",".",".",".",".",".",".","."],
           [".",".",".",".",".",".",".","."],
           [".",".",".","p",".",".",".","."],
           [".",".",".",".",".",".",".","."],
           [".",".",".",".",".",".",".","."]]
    out = 3
    actual = Solution().numRookCaptures(inp)
    assert actual == out, (actual, out)

    inp = [[".",".",".",".",".",".",".","."],
           [".","p","p","p","p","p",".","."],
           [".","p","p","B","p","p",".","."],
           [".","p","B","R","B","p",".","."],
           [".","p","p","B","p","p",".","."],
           [".","p","p","p","p","p",".","."],
           [".",".",".",".",".",".",".","."],
           [".",".",".",".",".",".",".","."]]
    out = 0
    actual = Solution().numRookCaptures(inp)
    assert actual == out, (actual, out)

    inp = [[".",".",".",".",".",".",".","."],
           [".",".",".","p",".",".",".","."],
           [".",".",".","p",".",".",".","."],
           ["p","p",".","R",".","p","B","."],
           [".",".",".",".",".",".",".","."],
           [".",".",".","B",".",".",".","."],
           [".",".",".","p",".",".",".","."],
           [".",".",".",".",".",".",".","."]]
    out = 3
    actual = Solution().numRookCaptures(inp)
    assert actual == out, (actual, out)

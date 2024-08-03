# 08/03/2024
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ans = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] =='X' and (i==0 or board[i-1][j] == '.') and (j==0 or board[i][j-1] == '.'):
                    ans += 1
        return ans

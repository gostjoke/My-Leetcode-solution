### not finished yet 
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@date         :2023/04/25 15:53:15
@date         :2025/06/12 finished....
'''

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for i in range(9):
            rtol = []
            top = []
            for j in range(9):
                r = board[i][j]
                if r !='.' and r in rtol:
                    return False
                elif r != '.':
                    rtol.append(r)
                t = board[j][i]
                if t !='.' and t in top:
                    return False
                elif t != '.':
                    top.append(t)    
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        val = board[box_row + i][box_col + j]
                        if val != '.':
                            if val in seen:
                                return False
                            seen.add(val)

        return True               
                

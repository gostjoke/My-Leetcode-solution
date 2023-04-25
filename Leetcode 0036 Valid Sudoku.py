### not finished yet 
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@date         :2023/04/25 15:53:15
'''
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for row in range(9):
            # row test
            list_test = [i for i in board[row] if i != "."]
            if len(set(list_test)) == len(list_test):
                pass
            else:
                print(1)
                return False
            # col test
            a = []
            for col in range(9):

                if board[col][row] not in a:
                    a.append(board[col][row])
                elif board[col][row] == ".":
                    pass
                else:
                    print(2)
                    return False
            # from left cornor top to right bottom corner
            b = []

            if board[row][row] not in b:
                b.append(board[row][row])
            elif board[row][row] ==".":
                pass
            else:
                print(3)
                return False
            ## form right cornor to left bottom corner
            c= []
            if board[row][8-row] not in c:
                c.append(board[row][8-row])
            elif board[row][8-row] == ".":
                pass
            else:
                print(4)
                return False
            
        return True

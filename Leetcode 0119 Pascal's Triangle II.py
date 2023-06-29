'''
2023/06/29
'''

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rowIndex += 1
        if rowIndex == 1:
           return[1]
        elif rowIndex == 0:
            return[1,1]


        df = [[1]*(i+1) for i in range(rowIndex)]

        for x in range(2, rowIndex):
            for j in range(1, x):
                df[x][j] = df[x-1][j-1] + df[x-1][j]
        
        return df[-1]

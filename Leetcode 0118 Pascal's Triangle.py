'''
06/23/2023
'''

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]*(i+1) for i in range(numRows)]

        for x in range(numRows):
            if x < 2:
                continue
            for j in range(1, x):
                ans[x][j] = ans[x-1][j-1] + ans[x-1][j]
            
        return ans

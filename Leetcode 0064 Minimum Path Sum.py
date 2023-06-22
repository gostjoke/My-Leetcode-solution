'''
6/22/2023
thanks to aryan_0077 image in leetcode 
'''

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ### use dp
        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if i > 0 and j > 0:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1]) ## we add last min(top, left) to next

                elif i > 0:
                    grid[i][j] += grid[i-1][j]
                elif j > 0:
                    grid[i][j] += grid[i][j-1]

                print(i, j, grid[i][j])
        return grid[-1][-1]

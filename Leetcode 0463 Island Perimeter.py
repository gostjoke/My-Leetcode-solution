"""
06/04/2023
"""

class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        ans = [[0] * n for j in range(m)]
        ## record ans in each cell
        for i in range(m):
            for j in range(n):
                ## water
                if grid[i][j] == 0:
                    ans[i][j] = 0

                else:
                    if i == 0 or (i > 0 and grid[i-1][j] == 0):# cell's top
                        ans[i][j] += 1
                    if j == 0 or (j > 0 and grid[i][j-1] == 0):# cell's left
                        ans[i][j] += 1
                    if i == m -1 or (i < m-1 and grid[i+1][j] == 0): # cell's bottom
                        ans[i][j] += 1
                    if j == n -1 or (j < n-1 and grid[i][j+1] == 0): # cell's right
                        ans[i][j] += 1
        return sum([sum(a) for a in ans])
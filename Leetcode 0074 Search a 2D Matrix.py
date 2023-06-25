"""
06/24/2023
"""
### better solution
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) - 1
        n = len(matrix[0]) - 1
        x,y = 0,0
        while True:
            if matrix[y][x] == target:
                return True
            elif matrix[y][x] != target and x < n:
                x += 1
            elif matrix[y][x] != target and x == n and y < m:
                y += 1
                x = 0
            elif y == m and x == n and matrix[y][x] != target:
                return False


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == target:
                    return True

        return False            

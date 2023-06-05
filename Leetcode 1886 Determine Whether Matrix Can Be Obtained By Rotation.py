"""
06/05/2023
explain@: 
"""

class Solution:
    def findRotation(self, mat: list[list[int]], target: list[list[int]]) -> bool:
        if mat == target:
            return True
        for i in range(3):
            mat = self.rotate(mat)
            if mat == target:
                return True
        return False

    def rotate(self, matrix: list[list[int]]) -> list:
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j] ## exchange
        for i in matrix:
            i.reverse()
        return matrix

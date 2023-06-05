"""
06/05/2023
explain@: 
"""

class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j] ## exchange
        """
        [1,2,3]     [1,4,7]
        [4,5,6]  -> [2,5,8]
        [7,8,9]     [3,6,9]
        """ 
        for i in matrix:
            i.reverse()
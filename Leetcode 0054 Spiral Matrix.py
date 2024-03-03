"03/03/2024"

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output =[]
        while matrix:
            output += matrix.pop(0)
            matrix = (list(zip(*matrix)))[::-1]
            print(matrix)
        return output
                

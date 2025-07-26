# 20250726, chatgpt helped, need to practice more
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]*n for _ in range(n)]
        top, bot = 0, n-1
        left, right = 0, n-1
        num = 1
        max_num = n*n

        while num <= max_num:
            # fill to right
            for i in range(left, right+1):
                matrix[top][i] = num
                num += 1
            top += 1

            for  i in range(top, bot+1):
                matrix[i][right] = num
                num += 1
            right -= 1

            for i in range(right, left-1, -1):
                matrix[bot][i] = num
                num += 1
            bot -= 1

            for i in range(bot, top-1, -1):
                matrix[i][left] = num
                num += 1
            left += 1
        return matrix


            

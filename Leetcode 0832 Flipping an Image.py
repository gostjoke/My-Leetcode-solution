"""
06/05/2023
explain@: 

Time complexity:
O(n^2)

Space complexity:
O(1)
"""

class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        for i in image:
            i.reverse()
        n = len(image)
        for x in range(n):
            for y in range(n):
                if image[x][y] == 1:
                    image[x][y] = 0
                else:
                    image[x][y] = 1
        return image
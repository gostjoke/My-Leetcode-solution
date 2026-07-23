# 2026/07/23
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        axis = [0,0]
        for i in moves:
            if i == "R":
                axis[0] += 1
            elif i == "L":
                axis[0] -= 1
            elif i == "U":
                axis[1] += 1
            elif i == "D":
                axis[1] -= 1

        return axis == [0,0]

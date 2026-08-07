# 2026/07/31
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return s in goal+goal

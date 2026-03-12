# 2026/03/12
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = [0] * 26
        for i in s:
            ld = ord(i)-97
            if seen[ld] != 0:
                return i
            else:
                seen[ld] = 1



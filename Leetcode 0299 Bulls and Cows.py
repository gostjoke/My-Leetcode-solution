# 08/03/2024
class Solution:
    def getHint(self, s: str, g: str) -> str:
        d1, d2, a, b = defaultdict(int), defaultdict(int), 0, 0
        for i, j in zip(s, g):
            if i == j:
                a += 1
            else:
                d1[i] += 1
                d2[j] += 1
        for i in d1:
            if i in d2:
                b += min(d1[i], d2[i]) 
        return f"{a}A{b}B"


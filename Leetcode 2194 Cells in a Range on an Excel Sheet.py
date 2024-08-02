## 08/02/2024

class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        ans = []
        for cha in range((ord(s[0])-64), (ord(s[3])-64)+1):
            for num in range(int(s[1]), int(s[4])+1):
                ans.append(chr(cha+64) + str(num))

        return ans

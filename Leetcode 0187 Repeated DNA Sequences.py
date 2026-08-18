# 2025/08/17
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        ans = set()
        if len(s) < 11:
            return []
        for i in range(0, len(s)-9):
            num = s[i:i+10]
            if num in seen:
                ans.add(num)
            seen.add(num)
            
        return list(ans)

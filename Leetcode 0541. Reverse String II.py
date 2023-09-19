"""
09/19/2023
"""

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans = ""
        n = math.ceil(len(s)/k)
        for i in range(n):
            if i % 2 == 0:
                ans += s[k*i:k*(i+1)][::-1]
            else:
                ans += s[k*i:k*(i+1)]
        
        return ans

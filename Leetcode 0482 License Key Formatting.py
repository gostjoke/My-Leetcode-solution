# 20250804
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s_r = s.replace("-", "").upper()
        if len(s_r) <= k:
            return s_r

        
        left = len(s_r) % k
        ans = []
        if left != 0:
            ans.append(s_r[:left]+"-")
        count = 0
        for i in s_r[left:]: 
            if count == k:
                ans.append("-")
                count = 0
            ans.append(i)  
            count += 1
        
        return "".join(ans)

'''
06/30/2023
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        ## slide windows
        l = 0
        r = 1
        max_s = 0
        for i in range(len(s)):
            ans = s[l:r+i]
            if len(set(ans)) != len(ans):
                l += 1
            if len(s[l:r+i]) > max_s:
                max_s = len(ans)
        
        return max_s
            

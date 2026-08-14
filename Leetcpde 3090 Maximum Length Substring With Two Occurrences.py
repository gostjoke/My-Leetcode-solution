# 2026/08/14
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        freq = [0]*26
        l = 0
        ans = 0
        for r in range(len(s)):
            index = ord(s[r])  - 97
            freq[index] += 1
            while freq[index] > 2:
                freq[ord(s[l])-97] -= 1
                l += 1
            ans = max(ans, r-l+1)
        return ans

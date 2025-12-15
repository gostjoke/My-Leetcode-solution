# 2025/12/15
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans = []
        arow="qwertyuiop"
        brow="asdfghjkl"
        crow="zxcvbnm"

        for word in words:
            nword = set(list(word))
            acheck=0
            bcheck=0
            ccheck=0
            for c in nword:
                c = c.lower()
                if c in arow:
                    acheck = 1
                elif c in brow:
                    bcheck = 1
                elif c in crow:
                    ccheck = 1
            if (acheck + bcheck + ccheck) == 1:
                ans.append(word)
        return ans
            

# 2026/03/12
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        odd = 0
        w1 = [i for i in word1]
        w2 = [i for i in word2]
        while w1 or w2:
            if not w2:
                ans += w1.pop(0)
            elif not w1:
                ans += w2.pop(0)
            elif odd == 0:
                ans += w1.pop(0)
                odd = 1
            else:
                ans += w2.pop(0)
                odd = 0
        return ans             



'''
06/27/2023
'''

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        if len(word1) >= len(word2):
            word2 += "_"*(len(word1) - len(word2))
            for i, j in zip(word1,word2):
                if j != "_":
                    ans += (i+j)
                else:
                    ans += i


        elif len(word1) < len(word2):
            word1 += "_"*(len(word2) - len(word1))
            for i, j in zip(word1,word2):
                if i != "_":
                    ans += (i+j)
                else:
                    ans += j

        return ans

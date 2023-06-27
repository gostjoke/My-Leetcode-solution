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

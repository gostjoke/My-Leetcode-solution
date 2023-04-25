#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@date         :2023/04/24 11:40:20
'''

class Solution:
    def sortSentence(self, s: str) -> str:
        li = s.split(" ")
        ans = [""]*len(li)
        for i in li:
            ans[int(i[-1])-1] = i[:-1]
        return " ".join(ans)
    
print(Solution().sortSentence("is2 sentence4 This1 a3"))

# very easy question
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@date         :2023/06/05 11:12:57
'''

class Solution:
    def removeAnagrams(self, words: list[str]) -> list[str]:
        ans = []
        for ind, i in enumerate(words):
            if ind == 0:
                ans.append(i)
            elif ''.join(sorted(words[ind-1])) != ''.join(sorted(i)):
                ans.append(i)
        
        return ans
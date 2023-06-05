#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@date         :2023/06/05 10:47:57
'''

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        if len(strs) == 1: # for only 1 word, make this faster XD
            return [strs]

        ans = []
        dic = {}
        for word in strs:
            sortedwords = ''.join(sorted(word))  ## make the list to word
            if sortedwords not in dic:
                dic[sortedwords] = [word]
            else:
                dic[sortedwords].append(word)

        for i in dic.values():
            ans.append(i)

        return ans

    
a = Solution().maxArea(height=[1,8,6,2,5,4,8,3,7])
print(a)
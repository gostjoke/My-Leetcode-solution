#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@explain      :97.14%, Memory 13.8 Beats 97.12%
@date         :2023/04/22 22:01:20

'''
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = s.split(" ")
        for i in a[::-1]:
            if i != "":
                return len(i)


print(Solution().lengthOfLastWord(s="   fly me   to   the moon  "))
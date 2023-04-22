#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@explain      :5.6%, Memory14.9 Beats 56.67%
@date         :2023/04/20 11:31:20

'''
#very bad...
class Solution:
    def isValid(self, s: str) -> bool:
        while len(s) > 0:
            li = len(s)
            s = s.replace("{}","").replace("()","").replace("[]","")
            if len(s) == 0:
                return True
            elif li == len(s):
                return False
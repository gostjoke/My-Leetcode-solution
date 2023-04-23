#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@explain      :26 ms 89%, Memory 13.8 Beats 42.6%
@date         :2023/04/23 00:03:20

'''
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        a = ""
        while columnNumber > 0:
            tmp = columnNumber%26
            if tmp == 0:
                tmp = 26
                columnNumber //=26
                columnNumber -= 1 
            else:
                columnNumber //=26
            a += chr(64+tmp)
    
            if tmp == 26 and columnNumber < 1:
                break

        return a[::-1]
print(Solution().convertToTitle(columnNumber=701))

### I take it as 26 Positional notation to calculate, 

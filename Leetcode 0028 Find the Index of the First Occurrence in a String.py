#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@explain      :16.10%, Memory 13.8 Beats 94.26%
@date         :2023/04/22 11:31:20

'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        li = len(needle) # need to know needle len
        for i in range(len(haystack) - li +1):  # 9 -3
            if haystack[i:i+li] == needle:
                return i
        else:
            return -1

# it is check every li words to see is it corresond to haystack

    
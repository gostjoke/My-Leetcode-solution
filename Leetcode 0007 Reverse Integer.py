#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@explain      :Beats 63.22%, 13.9 MB beat 48.7%
@date         :2023/04/24 11:44:55
'''

class Solution:
    def reverse(self, x: int) -> int:      
        if str(x)[0] == "-":
            ans = int("-" + (str(x)[1:][::-1]) )
        else:
            ans = int(str(x)[::-1])
        if ans < (-2)**31: return 0
        elif ans > ((2)**31 -1):return 0
        else: return ans
        

#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@explain      :
@date         :2022/10/06 
'''
class Solution:
    def isHappy(self, n: int) -> bool:
        a = []
        while n not in a:
            a.append(n)
            n = sum([int(i)**2 for i in str(n)])
        return True if n == 1 else False



print(Solution().isHappy(n=19))
    
## it is the standard easy way to deal but not good
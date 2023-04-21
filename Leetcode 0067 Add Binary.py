#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@explain      :
@date         :2023/04/21 14:35:47
@author       :
@version      :1.0
'''


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2) + int(b,2))[2:] 
    
print(Solution().addBinary(a = "11", b = "1"))

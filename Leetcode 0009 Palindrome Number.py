#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@explain      :20.84%
@date         :2023/04/20 11:31:20
@author       :
@version      :1.0
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        left = 0
        right = len(x) -1
        
        if x[0] == "-":
            return False
        for i in range(len(x)//2):
            if x[left+i] == x[right-i]:
                pass
            else:
                return False
        return True 
    
'''        
@explain      :18.59%
@date         :2023/04/20 11:31:20
@author       :
@version      :1.0
'''        
class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = [i for i in str(x)]
        b = [i for i in str(x)] 
        a.reverse()
        if a == b:
            return True
        else:
            return False

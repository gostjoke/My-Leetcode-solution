#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@explain      :beat 84.85%, memory beat 92.69%
@date         :2023/04/21 11:56:58
@author       :
@version      :1.0
'''

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        a = len(digits) # ['4','2'] will be 42
        counter = 0
        for ind, i in enumerate(digits):
            counter += i*(10**(a-1-ind))            
        counter += 1
        
        ans = [int(i) for i in str(counter)]
        return ans
        
bbb = Solution().plusOne(digits=[9])

print(bbb)
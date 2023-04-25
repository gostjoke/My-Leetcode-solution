#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@explain      :
@date         :2023/04/21 
@author       :
@version      :1.0
'''
class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 0:
            return 0
        elif x <=3:
            return 1
        elif x <= 8:
            return 2
        n = x//2 
        for i in range(n):
            if (i * i) == x:
                return i
            elif (i * i) > x:
                return (i-1)
            
print(Solution().mySqrt(x = 9))

### kind a little stupid....
### change to binary search
class Solution:
    def mySqrt(self, x: int) -> int:
        #### save some memory
        if x <= 0:
            return 0
        elif x <=3:
            return 1
        elif x <= 8:
            return 2
        right = x
        ######
        left = 3
        while right >= left:
            middle = (right + left)//2
            if middle*middle == x:
                return middle
            elif middle*middle > x:
                right = middle - 1
            else:
                left = middle + 1
        return right

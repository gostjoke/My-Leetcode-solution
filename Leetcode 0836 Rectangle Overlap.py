#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@explain      :
@date         :2023/06/07 11:44:44
@version      :1.0
'''

class Solution:
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        ## we just need to know what situation would not overlap

        """
        rec1 = [0,0,2,2], rec2 = [1,1,3,3]
        
        (-2,-2)      (3,-2)

        (-2, 0)      (3, 0)

                     (3,-1)    (6,-1)

                     (3,-4)    (6,-4)
        """ 
        if rec1[0] < rec2[2] and rec1[1] < rec2[3] and rec2[1] < rec1[3] and rec2[0] < rec1[2]:
            return True
        else:
            return False
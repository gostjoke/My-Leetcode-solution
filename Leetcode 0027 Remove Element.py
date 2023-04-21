#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@explain      :29.3%
@date         :2023/01/27 11:31:20
@author       :
@version      :1.0
'''
enumerate

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        count = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1 
        return count
    
Solution().removeElement(nums=[])

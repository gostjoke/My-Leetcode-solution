#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@explain      :
@date         :2023/06/01 14:50:04
'''

class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        area_max = 0
        while left < right:
            area_curr = min(height[left], height[right]) * (right - left)
            if area_max < area_curr:
                area_max = area_curr

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return area_max

    
a = Solution().maxArea(height=[1,8,6,2,5,4,8,3,7])
print(a)
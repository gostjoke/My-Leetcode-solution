#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@date         :2023/04/27 10:30:14
'''

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        min_po = max_po = -1
        for ind, i in enumerate(nums):
            if i == target and min_po == -1:
                min_po =  max_po = ind
            elif i == target:
                max_po = ind

        return [min_po, max_po]

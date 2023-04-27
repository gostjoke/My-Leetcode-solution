#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@date         :2023/04/27 10:30:14
'''

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        min_po = -1
        max_po = -1
        for ind, i in enumerate(nums):
            if i == target and min_po == -1:
                min_po = ind
                max_po = ind
            elif i == target:
                max_po = ind
        return [min_po, max_po]
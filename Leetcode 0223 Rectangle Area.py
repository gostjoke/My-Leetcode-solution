#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@file         :Leetcode 0223 Rectangle Area.py
@explain      :need to say some people's solution is really smart
@date         :2023/06/07 11:05:44
@version      :1.0
'''

# Definition for singly-linked list.
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        rec1 = abs(ax2 - ax1) * abs(ay2-ay1)
        rec2 = abs(bx2 - bx1) * abs(by2-by1)
        # 4 coner (ax1,ay1) (ax2,ay1) (ax2,ay2) (ax1,ay2)

        overlap_width = min(ax2,bx2) - max(ax1, bx1)
        overlap_heigh = min(ay2,by2) - max(ay1, by1)
        over_area = max(overlap_width, 0) * max(overlap_heigh, 0)

        return rec1 + rec2 - over_area
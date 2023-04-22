#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@explain      :51.23%, Memory 13.8 Beats 96.84%
@date         :2023/04/22 11:31:20

'''

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == -1 and (dividend < -1):
            return dividend*(-1) - 1
        ans = str(dividend/divisor)
        a = ans.split(".")
        return int(a[0])

'''  
i found when dividend is negative and divisor is -1 will need to reduce 1,
but when dividend is -1 and divisor -1, it does not need, so I deal it in first if
'''

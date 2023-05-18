#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@explain      :
@date         :2023/05/16 11:31:20
@author       : 
@version      :1.0
'''


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            n = -n
            x = 1/x

        return x**n
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@explain      :Runtime 27 ms Beats 92.82%, Memory 13.7 Beats 89.9%
@date         :2023/04/23 00:22:20
'''

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        elif n <= 0:
            return False
        while n > 2:
            if n % 2 != 0: # odd number must wrong excpet 1
                return False
            n /= 2
        if n % 2 == 0:
            return True
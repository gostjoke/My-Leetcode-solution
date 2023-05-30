#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@explain      :
@date         :2023/05/30 15:51:48
'''

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        fact_list = [i for i in range(1, n+1) if n % i == 0]
        if k > len(fact_list):
            return -1
        else:
            return fact_list[k-1]
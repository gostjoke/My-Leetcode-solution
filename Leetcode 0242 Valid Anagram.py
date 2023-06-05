#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@date         :2023/06/05 11:15:57
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return True if ''.join(sorted(s)) == ''.join(sorted(t)) else False
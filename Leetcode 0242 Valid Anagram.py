#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# 2025/07/16 update
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0] * 26
        for c1, c2 in zip(s, t):
            count[ord(c1) - ord('a')] += 1
            count[ord(c2) - ord('a')] -= 1
        return all(i == 0 for i in count )

'''
@date         :2023/06/05 11:15:57
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return True if ''.join(sorted(s)) == ''.join(sorted(t)) else False

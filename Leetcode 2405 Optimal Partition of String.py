'''
06/30/2023
'''

class Solution:
    def partitionString(self, s: str) -> int:
        cur = set()
        res = 1
        for i in s:
            if i in cur:
                cur = set()
                res += 1
            cur.add(i)

        return res

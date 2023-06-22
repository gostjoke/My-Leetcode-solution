'''
06/22/2023
'''
class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            if 'inf' in s.lower():
                return False
            float(s)
            return True
        except:
            return False

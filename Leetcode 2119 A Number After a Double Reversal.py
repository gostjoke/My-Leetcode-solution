"""
06/05/2023
explain@: it is my best understanding

Time complexity:
O(1)

Space complexity:
O(1)
"""

class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if len(str(num)) == len(str(int(str(num)[::-1]))):
            return True
        else:
            return False
        
## second way

class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if str(num)[-1] == "0" and num != 0:
            return False
        else:
            return True
    
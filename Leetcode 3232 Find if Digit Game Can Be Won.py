# 08/06/2024
class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        count_single = 0
        count_double = 0
        for i in nums:
            if len(str(i)) == 1:
                count_single += i
            else:
                count_double += i
        return count_single != count_double

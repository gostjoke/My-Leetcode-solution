# 2026/08/22
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        dig_sum = 0
        dig_pro = 1
        for i in str(n):
            dig_sum += int(i)
            dig_pro *= int(i)
        return n % (dig_sum+dig_pro) == 0
            

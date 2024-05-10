# 05/10/2024

class Solution:
    def binaryGap(self, n: int) -> int:
        a = bin(n)[2:]
        ans = 0
        count = 0
        check = False
        for i in range(len(a)):
            if not check and a[i] == "1":
                check = True
            elif check and a[i] != "1":
                count +=1
            elif check and a[i] == "1":
                count +=1
                ans = max(ans, count)
                count = 0
        return ans

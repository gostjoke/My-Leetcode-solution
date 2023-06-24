"""
06/23/2023
"""
class Solution:
    def fib(self, n: int) -> int:
        ans =[]
        counter = 0
        for i in range(n+1):
            if i == 0:
                ans.append(0)
            elif i == 1:
                ans.append(1)
            elif i == 2:
                ans.append(1)
            else:
                ans.append(ans[counter-1]+ans[counter-2])
            counter += 1
        return ans[counter-1]

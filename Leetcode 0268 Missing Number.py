"""
I know it is stupid...
2023/06/14
"""

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        ans = [j for j in range(len(nums)+1)]
        for i in nums:
            try:
                ans.remove(i)
            except:
                pass
        return ans[0]
        
            
a = Solution().missingNumber(nums=[9,6,4,2,3,5,7,0,1])
print(a)

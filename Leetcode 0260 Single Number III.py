'''
06/24/2023
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        dic = {}
        ans = []
        for i in nums:
            try:
                dic[i] += 1
            except:
                dic[i] = 1
        
        for i, j in dic.items():
            if j == 1:
                ans.append(i)
        return ans

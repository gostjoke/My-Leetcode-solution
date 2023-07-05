'''
07/05/2023
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        appear = len(nums)/3
        ans = []
        dic = {}
        for i in nums:
            try:
                dic[i] += 1
            except:
                dic[i] = 1

        for num, item in dic.items():
            
            if item > appear:
                ans.append(num)
        return ans
                

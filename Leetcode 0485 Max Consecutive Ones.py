'''
06/22/2023
'''
## better
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        counter = 0
        for i in nums:
            if i == 1:
                counter += 1
            elif i == 0 and counter != 0:
                counter = 0
                
            if counter > ans:
                ans = counter
        return ans

## worse solution
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        s = ''
        for i in nums:
            s += str(i)
        
        a = s.split('0')
        return max([len(i) for i in a])

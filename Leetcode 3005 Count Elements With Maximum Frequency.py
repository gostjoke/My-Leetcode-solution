# 08/03/2024
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        a = (max(nums)+1)*[0]
        for i in nums:
            a[i] += 1
        max_cur=0
        max_fre=1
        for j in a:
            if j > max_cur:
                max_cur = j
                max_fre = j
            elif j == max_cur:
                max_fre += j
        return max_fre


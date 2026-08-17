# 2026/08/17 

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        ans = []
        max_n = max(nums)
        min_n = min(nums)
        freq = [0] * (max_n - min_n + 1)
        if (max_n - min_n + 1) == len(nums):
            return []

        for i in nums:
            freq[i-min_n] = 1
        for index, j in enumerate(freq):
            if j == 0:
                ans.append(index+min_n)

        return ans

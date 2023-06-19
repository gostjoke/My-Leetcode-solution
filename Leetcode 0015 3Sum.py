"""
@explain: refer Mangosteen Python3 solution extend from sum 2; understand
"""

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = set()
        for i in range(len(nums)):
            l = i + 1   ## second number
            r = len(nums)-1 ## last number
            target = 0 - nums[i]
            while l < r:  # binary search
                if nums[l] + nums[r] == target:
                    ans.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1

                elif nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
        return  list(ans)

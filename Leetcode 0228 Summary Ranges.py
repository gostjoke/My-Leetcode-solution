# 20250806
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [f"{nums[0]}"]

        ans = []
        i = 0
        while i < len(nums):
            start = i
            while i + 1 <len(nums) and nums[i+1]-nums[i] == 1:
                i+=1
            if start == i:
                ans.append(f"{nums[i]}")
            else:
                ans.append(f"{nums[start]}->{nums[i]}")
            i += 1
        return ans

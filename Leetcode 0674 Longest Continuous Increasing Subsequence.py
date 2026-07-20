## 2026/07/20

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        longest =1
        tmp_count = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                tmp_count +=1
            else:
                tmp_count = 1
            longest = max(longest, tmp_count)
        return longest

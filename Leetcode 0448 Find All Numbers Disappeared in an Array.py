## 20250630

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return list(set(i+1 for i in range(len(nums))) - set(nums))

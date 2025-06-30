## 20250630
# O(n)  O(1)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in nums:
            index = abs(i) - 1
            nums[index] = abs(nums[index])*-1
        return [ind+1 for ind, i in enumerate(nums) if i > 0]
# O(n)  O(n)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return list(set(i+1 for i in range(len(nums))) - set(nums))

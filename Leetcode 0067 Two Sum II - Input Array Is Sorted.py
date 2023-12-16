"""
12/16/2023
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        2 pointer
        """
        i = 0
        j = len(numbers) - 1
        while j > i:
            s = numbers[i] + numbers[j]
            if s == target:
                return [i+1, j+1]
            elif s > target: # bez the list is sorted
                j -= 1
            elif s < target:
                i += 1
            else:
                return []

# 2026/08/20
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        n_map = {}
        for i in nums:
            if i in n_map:
                n_map[i] += 1
            else:
                n_map[i] = 1
        for index, item in n_map.items():
            if item % 2 == 1:
                return False
        return True

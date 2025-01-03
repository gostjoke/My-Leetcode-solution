# 2025/01/03
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for i, n in enumerate(nums):
            if n in dic and abs(i-dic[n])<=k:
                return True
            else:
                dic[n] = i
        return False

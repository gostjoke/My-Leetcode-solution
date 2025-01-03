# 2025/01/02
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        for i in range(1,n+1):
            nums1[m-1+i] = nums2[i-1]
        nums1 = nums1.sort()
        return nums1

"""
12/14/2023
"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        Heap = []
        for num in nums:
            heapq.heappush(Heap, num)
            if len(Heap) > k:
                heapq.heappop(Heap)

        return Heap[0]

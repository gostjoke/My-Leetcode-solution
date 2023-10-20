class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        prev_f = sum([i*nums[i] for i in range(n)])
        max_f = prev_f

        for i in range(1, n):
            prev_f += total - (n * nums[n-i])
            max_f = max(prev_f, max_f)

        
        return max_f

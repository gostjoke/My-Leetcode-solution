# 2026/08/17
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_n = 0
        max_n_index = float("-inf")
        s_max_n = 0
        for index, n in enumerate(nums):
            if max_n < n:
                max_n, s_max_n = n, max_n
                max_n_index = index
            elif max_n > n > s_max_n:
                s_max_n = n
        # print(max_n, s_max_n)
        if s_max_n != 0:
            if max_n / s_max_n >= 2.0:
                return max_n_index
            else:
                return -1
        else: # prevent 0 
            if max_n == 0:
                return -1
            else:
                return max_n_index

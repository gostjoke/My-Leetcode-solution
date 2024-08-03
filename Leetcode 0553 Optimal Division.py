# 08/03/2024
class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        if len(nums) == 1:
            return f"{nums[0]}"
        elif len(nums) == 2:
            return f"{nums[0]}/{nums[1]}"
        num = list(map(str, nums))
        a = f"{num[0]}/(" 
        for i in num[1:]:
            a += f"{i}/"
        a = a[:-1]
        a += ")"
        return a

"""
06/05/2023
explain@: only use 1 for, no sort() good!
"""

class Solution:
    def average(self, salary: list[int]) -> float:
        ave = len(salary) - 2
        max_s, min_s = 0, 1000000
        for i in salary:
            if max_s < i:
                max_s = i
            if min_s > i:
                min_s = i 
        salary.append(max_s*-1)
        salary.append(min_s*-1)

        return sum(salary)/ave
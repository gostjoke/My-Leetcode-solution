# 2026/07/23

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr_dic = {}
        count = 1
        for i in sorted(arr):
            if i not in arr_dic:
                arr_dic[i] = count
                count += 1

        return [arr_dic[i] for i in arr]

"""
10/03/2023
"""

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:

        def my_count(my_list:list) -> dict:
            my_list.sort()
            dic = {}
            for i in my_list:
                i = str(i)
                if i in dic:
                    dic[i] += 1
                else:
                    dic[i] = 1
            return dic
            
        nums1_dic = my_count(nums1)
        nums2_dic = my_count(nums2)

        result = []
        if len(nums1_dic) > len(nums2_dic):
            nums1_dic, nums2_dic = nums2_dic, nums1_dic

        for num, count in nums1_dic.items():
            if num in nums2_dic:
                for i in range(min(int(count), nums2_dic[num])):
                    result.append(int(num))
                    
                    
        return result 

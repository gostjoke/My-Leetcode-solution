# 04/13/2024
class Solution:
    def maximum69Number (self, num: int) -> int:
        num_str = [i for i in str(num)]
        for i in range(len(num_str)):
            if num_str[i] == "6":
                num_str[i] = "9"
                break
        return int(''.join(num_str))

# 06/04/2024
class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        def num_split(number:str):
            number_list = number.split("+")
            number_n, number_i = int(number_list[0]), int((number_list[1]).replace("i",""))
            return number_n, number_i
        num1_n, num1_i = num_split(num1)
        num2_n, num2_i = num_split(num2)
        number_part = num1_n*num2_n + -1*(num1_i*num2_i)
        i_part = (num1_n * num2_i) + (num2_n * num1_i)
        return f"{number_part}+{i_part}i"

        

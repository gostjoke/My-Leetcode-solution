# Eazy "04/23/2024"

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # "#"count
        def get_s(string:str) -> str: 
            s_list = []
            for i in string:
                if i != "#":
                    s_list.append(i)
                elif i == "#" and len(s_list)!= 0:
                    s_list.pop()
            return "".join(s_list)

        return True if get_s(s) == get_s(t) else False

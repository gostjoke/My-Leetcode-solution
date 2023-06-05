"""
06/05/2023
explain@: consider all situation.... a little stupid
"""

class Solution:
    def reorderSpaces(self, text: str) -> str:
        count = 0 # space
        for ind, i in enumerate(text):
            if i == " ":
                count += 1
        if count == 0:
            return text  ### like "a"

        text2 = text.split(" ")
        text2 = [w for w in text2 if w !=""]
        try:
            space_len = count // (len(text2)-1)
        except:
            return text.strip() + " "*count ### like "  hello"
        space_extra = count % (len(text2)-1)
        ans = ""
        for words in text2:
            ans += (" "*space_len + words)
        ans = ans.strip()
        ans += " "*space_extra
        return ans
            

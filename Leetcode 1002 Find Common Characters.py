### "03/04/2024"

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        hast = [0]*26
        for i in words[0]:
            hast[ord(i) - ord("a")] += 1
        for j in words[1:]:
            hast2 = [0]*26
            for x in j:
                hast2[ord(x) - ord("a")] += 1
            
            for ind in range(26):
                hast[ind] = min(hast[ind],hast2[ind])
        output = []
        for ind, i in enumerate(hast):
            if i != 0:
                output.extend([chr(97+ind)] * i)
        return output


    
        


    
        

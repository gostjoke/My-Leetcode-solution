# 05/26/2024
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        """ A:65  a:97"""
        for ind, i in enumerate(word):
            if ind == 0:
                if ord(i) < 97:
                    cap = True
                else:
                    cap = False
            
            if ind==1:
                if ord(i)<97:
                    cap2 = True
                else:
                    cap2 = False

                if not cap and cap2:
                    return False  

            if ind > 1:
                if cap and cap2 and ord(i)>96:
                    return False
                elif not cap and not cap2 and ord(i)<97:
                    return False
                elif cap and not cap2 and ord(i)<97:
                    return False

        return True



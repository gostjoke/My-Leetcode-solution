# 04/04/2024

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        cha = [chr(97+i) for i in range(26)]
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        dic = dict(zip(cha, code))
        ans = ["".join([dic[j] for j in i ]) for i in words]
        return len(set(ans))

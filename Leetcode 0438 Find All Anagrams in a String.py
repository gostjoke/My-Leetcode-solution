# 20250716
class Solution:
    # def isAnagram(self, s: str, t: str) -> bool:
    #     if len(s) != len(t):
    #         return False
    #     count = [0] * 26
    #     for c1, c2 in zip(s, t):
    #         count[ord(c1) - ord('a')] += 1
    #         count[ord(c2) - ord('a')] -= 1
    #     return all(i == 0 for i in count )

    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_s, len_p = len(s), len(p)
        if len_s < len_p:
            return []

        ans = []
        p_count = [0]*26
        s_count = [0]*26

        ## caculate when index = 0
        for i in range(len_p):
            p_count[ord(p[i]) - ord('a')] += 1
            s_count[ord(s[i]) - ord('a')] += 1

        if s_count == p_count:
            ans.append(0)

        for i in range(len_p, len_s):
            # add new chr
            s_count[ord(s[i]) - ord('a')] += 1
            # remove left side chr
            s_count[ord(s[i - len_p]) - ord('a')] -= 1

            if s_count == p_count:
                ans.append(i -len_p +1)

        return ans


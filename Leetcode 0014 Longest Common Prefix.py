class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        a = []
        for i in zip(*strs):
            if len(set(i)) != 1:
                break
            a.append(i[0])
        return ("".join(a))

a = Solution().longestCommonPrefix(strs = ["flower","flow","flight"])
print(a)
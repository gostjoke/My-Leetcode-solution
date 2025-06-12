#20250612
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        path = []
        def check(c):
            return c == c[::-1]
        
        def backtrack(start):
            # set stop condition
            if start == len(s):
                ans.append(path[:])
                return

            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if check(substring):
                    path.append(substring)
                    backtrack(end)
                    path.pop()
        backtrack(0)
        return ans

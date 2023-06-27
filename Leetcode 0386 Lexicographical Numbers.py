"""
06/27/2023
I know it require O(1) speace and O(n), I will improve in the future
"""
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = [str(i) for i in range(1,n+1)]
        ans.sort()
        return [int(i) for i in ans]

'''
06/25/2023
'''

from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        letter_counts = Counter(s)
        ans = ""
        for l, count in letter_counts.most_common():
            ans += l*count

        return ans

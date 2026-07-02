# 2026/07/02
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        mapping = {}
        cur = head
        # build all node
        while cur:
            mapping[cur] = Node(cur.val)
            cur = cur.next
        # check Random
        cur = head
        while cur:
            mapping[cur].next = mapping.get(cur.next)
            mapping[cur].random = mapping.get(cur.random)
            cur = cur.next 
        # current head is the first node
        return mapping[head]
        


# 2025/01/02

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # first we need to get the length of head
        if not head:
            return None

        LE = head
        leng = 1
        a = [head.val]
        while LE.next:
            LE = LE.next
            leng += 1
            a.append(LE.val)
        
        k = k % leng
        LE.next = head

        steps_to_new_head = leng - k
        new_tail = head
        for _ in range(steps_to_new_head - 1):
            new_tail = new_tail.next
        # 新的頭節點
        new_head = new_tail.next
        # 斷開環
        new_tail.next = None

        return new_head

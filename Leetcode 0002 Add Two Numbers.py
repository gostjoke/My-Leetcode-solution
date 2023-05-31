#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Beat 50.60%
@date         :2023/05/31 12:53:12
@version      :1.0
@explain      :I think Convert to str then put it back to ListNode
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def node_to_str(ln) ->str:
            text1 = ''
            while ln:
                text1 += str(ln.val)
                ln = ln.next
            text1 = text1[::-1] 
            return text1

        node = str(int(node_to_str(l1))+ int(node_to_str(l2)))[::-1]

        dummy_head = ListNode(0)
        current = dummy_head
        for digit in node:
            current.next = ListNode(int(digit))
            current = current.next            

        return dummy_head.next
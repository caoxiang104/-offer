# -*- coding:utf-8 -*-
"""
输入两个链表，找出它们的第一个公共结点。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        while pHead2:
            temp_node = pHead1
            while temp_node:
                if temp_node.val == pHead2.val:
                    return temp_node
                temp_node = temp_node.next
            pHead2 = pHead2.next
        return None


s = Solution()
s1 = ListNode(2)
s1.next = ListNode(3)
s1.next.next = ListNode(4)
s2 = ListNode(5)
s2.next = ListNode(4)
s2.next.next = ListNode(3)
print(s.FindFirstCommonNode(s1, s2).val)
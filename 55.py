# -*- coding:utf-8 -*-
"""
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
链表值唯一确定
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        value = []
        head = pHead
        while head:
            if head.val in value:
                return head
            else:
                value.append(head.val)
                head = head.next
        return None


s = Solution()
list_ = ListNode(1)
list_.next = ListNode(2)
list_.next.next = ListNode(3)
list_.next.next.next = list_.next
print(s.EntryNodeOfLoop(list_).val)
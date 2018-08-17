# -*- coding:utf-8 -*-
"""
输入一个链表，反转链表后，输出新链表的表头。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        temp_node = pHead
        head = None
        while temp_node:
            temp = ListNode(temp_node.val)
            temp.next = head
            head = temp
            temp_node = temp_node.next
        return head


s = Solution()
node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
print(s.ReverseList(node))
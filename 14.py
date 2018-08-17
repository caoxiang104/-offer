# -*- coding:utf-8 -*-
"""
输入一个链表，输出该链表中倒数第k个结点。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        temp_node = head
        n = 0
        while temp_node:
            n += 1
            temp_node = temp_node.next
        i = n - k
        if i < 0:
            return None
        else:
            while i > 0:
                head = head.next
                i -= 1
            return head


s = Solution()
node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
print(s.FindKthToTail(node, 2))
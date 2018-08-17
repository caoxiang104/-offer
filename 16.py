# -*- coding:utf-8 -*-
"""
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        temp = ListNode(None)
        head = temp
        while pHead1 and pHead2:
            if pHead1.val < pHead2.val:
                temp_node = ListNode(pHead1.val)
                temp.next = temp_node
                temp = temp.next
                pHead1 = pHead1.next
            else:
                temp_node = ListNode(pHead2.val)
                temp.next = temp_node
                temp = temp.next
                pHead2 = pHead2.next
        while pHead1:
            temp_node = ListNode(pHead1.val)
            temp.next = temp_node
            temp = temp.next
            pHead1 = pHead1.next
        while pHead2:
            temp_node = ListNode(pHead2.val)
            temp.next = temp_node
            temp = temp.next
            pHead2 = pHead2.next
        return head.next


s = Solution()
node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node1 = ListNode(1)
node1.next = ListNode(2)
node1.next.next = ListNode(3)
head = s.Merge(node, node1)
while head:
    print(head.val)
    head = head.next
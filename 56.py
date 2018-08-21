# -*- coding:utf-8 -*-
"""
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，
重复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5
处理后为 1->2->5
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if not pHead:
            return None
        while pHead and pHead.next and pHead.val == pHead.next.val:  # 处理1112233类似情况
            while pHead.next and pHead.val == pHead.next.val:  # 指针指向最后一个重复如111中的最后一个1
                pHead = pHead.next
            pHead = pHead.next  # 跳出重复，如1112指向2
        if pHead:  # 判断是否为空
            head = pHead
            next_node = pHead.next
        else:
            return None
        while next_node:
            if next_node.next and next_node.val == next_node.next.val:
                while next_node.next and next_node.val == next_node.next.val:
                    next_node = next_node.next
                next_node = next_node.next
                pHead.next = next_node
            else:
                pHead = pHead.next
                next_node = next_node.next
        return head


s = Solution()
list_ = ListNode(1)
list_.next = ListNode(2)
list_.next.next = ListNode(3)
list_.next.next.next = ListNode(3)
list_ = s.deleteDuplication(list_)
while list_:
    print(list_.val, end=" ")
    list_ = list_.next
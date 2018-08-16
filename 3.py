# -*- coding:utf-8 -*-
"""输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here

        def recurse(node, list_):
            if node:
                recurse(node.next, list_)
                list_.append(node.val)
            return list_

        return recurse(listNode, [])


s = Solution()
listNode = ListNode(67)
listNode.next = ListNode(0)
listNode.next.next = ListNode(24)
listNode.next.next.next = ListNode(58)
print(s.printListFromTailToHead(listNode))
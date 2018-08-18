# -*- coding:utf-8 -*-
"""
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，
另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。
（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
"""


class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if pHead:
            head = RandomListNode(None)
            temp = head
        else:
            return None
        while pHead:
            temp.next = RandomListNode(pHead.label)
            temp.next.next = pHead.next
            temp.next.random = pHead.random
            temp = temp.next
            pHead = pHead.next
        return head.next


s = Solution()
head = RandomListNode(2)
head.next = RandomListNode(3)
head.random = RandomListNode(5)
head.next.next = RandomListNode(4)
head.next.random = RandomListNode(5)
out = s.Clone(head)
while out:
    print(out.label, end=" ")
    if out.next:
        print(out.next.label, end=" ")
    if out.random:
        print(out.random.label)
    out = out.next
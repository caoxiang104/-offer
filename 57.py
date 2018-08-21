# -*- coding:utf-8 -*-
"""
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
"""


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return None
        if pNode.right: # 有右节点
            pNode = pNode.right
            while pNode.left: # 返回右节点的最左节点
                pNode = pNode.left
            return pNode  # 返回右子树的最左节点
        else:   # 无右节点
            if pNode.next == None:  # 头节点
                return None
            elif pNode.next.left == pNode:  # 父节点的左节点
                return pNode.next
            else: # 父节点的右节点
                while pNode.next and pNode.next.right == pNode:
                    pNode = pNode.next
                if pNode.next == None:  # 中序遍历最后一个节点
                    return None
                else:  # 返回中节点
                    return pNode.next


s = Solution()
tree = TreeLinkNode(5)
tree.left = TreeLinkNode(4)
tree.left.next = tree
tree.left.left = TreeLinkNode(3)
tree.left.left.next = tree.left
tree.left.left.left = TreeLinkNode(2)
tree.left.left.left.next = tree.left.left
node = s.GetNext(tree.left)
print(node.val)
# -*- coding:utf-8 -*-
"""
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的
双向链表。要求不能创建任何新的结点，只能调整树中结
点指针的指向。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return pRootOfTree
        list_ = []


        def inorder(node, list_):
            if node is not None:
                inorder(node.left, list_)
                list_.append(node)
                inorder(node.right, list_)
        inorder(pRootOfTree, list_)
        if len(list_) == 1:
            return list_[0]
        else:
            head = list_[0]
            head.left = None
            head.right = list_[1]
            for i in range(1, len(list_) - 1):
                list_[i].left = list_[i-1]
                list_[i].right = list_[i + 1]
            list_[len(list_) - 1].left = list_[len(list_) - 2]
        return head


s = Solution()
tree1 = TreeNode(8)
tree1.left = TreeNode(6)
tree1.right = TreeNode(14)
tree1.left.left = TreeNode(3)
tree1.left.right = TreeNode(7)
tree1.left.left.left = TreeNode(2)
tree1.left.left.right = TreeNode(5)
tree1.right.left = TreeNode(10)
tree1.right.right = TreeNode(15)
tree1.right.left.left = TreeNode(9)
tree1.right.left.right = TreeNode(12)
out = s.Convert(tree1)
while out.right:
    print(out.val, end=" ")
    out = out.right
print(out.val)
while out:
    print(out.val, end=" ")
    out = out.left


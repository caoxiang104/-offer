# -*- coding:utf-8 -*-
"""
输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0
        d = 1
        listd = []
        self.depth(pRoot, d, listd)
        return max(listd)

    def depth(self, root, d, listd):
        if not root.left and not root.right:
            listd.append(d)
        else:
            if root.left:
                self.depth(root.left, d + 1, listd)
            if root.right:
                self.depth(root.right, d + 1, listd)


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
print(s.TreeDepth(tree1))
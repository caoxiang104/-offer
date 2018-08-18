# -*- coding:utf-8 -*-
"""
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        out = []
        list1 = [root]
        while list1:
            node = list1.pop(0)
            if node:
                out.append(node.val)
                if node.left:
                    list1.append(node.left)
                if node.right:
                    list1.append(node.right)
        return out


s = Solution()
tree1 = TreeNode("8")
tree1.left = TreeNode("8")
tree1.right = TreeNode("7")
tree1.left.left = TreeNode("9")
tree1.left.right = TreeNode("2")
tree1.left.left.left = TreeNode("#")
tree1.left.left.right = TreeNode("#")
tree1.left.right.left = TreeNode("#")
tree1.left.right.right = TreeNode("#")
tree1.right.left = TreeNode("#")
tree1.right.right = TreeNode("#")
print(s.PrintFromTopToBottom(tree1))
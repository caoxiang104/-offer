# -*- coding:utf-8 -*-
"""
操作给定的二叉树，将其变换为源二叉树的镜像。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root.left or root.right:
            temp = root.left
            root.left = root.right
            root.right = temp
        if root.left:
            self.Mirror(root.left)
        if root.right:
            self.Mirror(root.right)
        return root


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
tree2 = TreeNode("8")
tree2.left = TreeNode("9")
tree2.right = TreeNode("2")
tree = s.Mirror(tree1)
list1 = [tree]
while list1:
    node = list1.pop(0)
    if node:
        print(node.val, end=" ")
    if node.left:
        list1.append(node.left)
    if node.right:
        list1.append(node.right)
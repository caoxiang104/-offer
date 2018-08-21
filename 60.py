# -*- coding:utf-8 -*-
"""
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        pri = []
        queue = [pRoot]
        index_list = [0]
        temp_list = []
        while queue:
            node = queue.pop(0)
            index = index_list.pop(0)
            if not index_list or index != index_list[0]:
                temp_list.append(node.val)
                pri.append(temp_list)
                temp_list = []
            else:
                temp_list.append(node.val)
            if node.left:
                queue.append(node.left)
                index_list.append(index + 1)
            if node.right:
                queue.append(node.right)
                index_list.append(index + 1)
        return pri


s = Solution()
tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(2)
tree.left.left = TreeNode(3)
tree.left.right = TreeNode(4)
tree.right.left = TreeNode(4)
tree.right.right = TreeNode(3)
print(s.Print(tree))

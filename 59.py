# -*- coding:utf-8 -*-
"""
请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，
第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他
行以此类推。
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
        out = []
        for i in range(len(pri)):
            if i % 2 == 1:
                out.append(pri[i][::-1])
            else:
                out.append(pri[i])
        return out


s = Solution()
tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(2)
tree.left.left = TreeNode(3)
tree.left.right = TreeNode(4)
tree.right.left = TreeNode(4)
tree.right.right = TreeNode(3)
print(s.Print(tree))
# -*- coding:utf-8 -*-
"""
给定一棵二叉搜索树，请找出其中的第k小的结点。例如， （5，3，7，2，4，6，8）    中，按结点数值大小顺序第三小结点的值为4。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回对应节点TreeNode
    def __init__(self):
        self.out = []
        self.length = 0

    def KthNode(self, pRoot, k):
        # write code here
        self.dfs(pRoot)
        return self.out[k - 1] if self.length >= k else None

    def dfs(self, pRoot):
        if pRoot:
            self.dfs(pRoot.left)
            self.out.append(pRoot)
            self.length += 1
            self.dfs(pRoot.right)
        else:
            return None


s = Solution()
tree1 = TreeNode(8)
tree1.left = TreeNode(6)
tree1.right = TreeNode(10)
tree1.left.left = TreeNode(5)
tree1.left.right = TreeNode(7)
tree1.right.left = TreeNode(9)
tree1.right.right = TreeNode(11)
print(s.KthNode(tree1, 2).val)
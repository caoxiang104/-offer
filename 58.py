# -*- coding:utf-8 -*-
"""
请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if not pRoot:
            return True
        return self.symmetrical(pRoot.left, pRoot.right)

    def symmetrical(self, left, right):
        if not left and not right:
            return True
        elif not left or not right:
            return False
        else:
            if left.val == right.val:
                return self.symmetrical(left.left, right.right) and self.symmetrical(left.right, right.left)
            else:
                return False


s = Solution()
tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(2)
tree.left.left = TreeNode(3)
tree.left.right = TreeNode(4)
tree.right.left = TreeNode(4)
tree.right.right = TreeNode(3)
print(s.isSymmetrical(tree))
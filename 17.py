# -*- coding:utf-8 -*-
"""
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2:
            return False
        val = pRoot2.val

        def recurse(pRoot1, val, list_):
            if pRoot1.val == val:
                list_.append(pRoot1)
            if pRoot1.left:
                recurse(pRoot1.left, val, list_)
            if pRoot1.right:
                recurse(pRoot1.right, val, list_)
        list_ = []
        recurse(pRoot1, val, list_)
        index = 0
        for list_temp in list_:
            list2 = [list_temp]
            list1 = [pRoot2]
            while list1:
                node1 = list1.pop(0)
                node2 = list2.pop(0)
                if node1 and not node2:
                    index = 1
                    break
                if node1.val != node2.val:
                    index = 1
                    break
                if node1.left:
                    list1.append(node1.left)
                    if not node2.left:
                        index = 1
                        break
                    list2.append(node2.left)
                if node1.right:
                    list1.append(node1.right)
                    if not node2.right:
                        index = 1
                        break
                    list2.append(node2.right)
            if index == 0:
                return True
            index = 0
        return False


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
print(s.HasSubtree(tree1, tree2))
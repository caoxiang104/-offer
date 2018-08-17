# -*- coding:utf-8 -*-
"""
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例
如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,
2,1,5,3,8,6}，则重建二叉树并返回
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here

        def recurse(pre, tin, node):
            if pre:
                temp_node = TreeNode(pre[0])
                node = temp_node
                index = tin.index(pre[0])
                left = tin[:index]
                right = tin[index + 1:]
                pre.pop(0)
                if len(left) > 0:
                    node.left = recurse(pre, left, node.left)
                if len(right) > 0:
                    node.right = recurse(pre, right, node.right)
            return node

        node = recurse(pre, tin, None)
        # list_ = []
        # temp = []
        # temp.append(node)
        #
        # def level(temp, list_):
        #     if temp:
        #         node = temp.pop(0)
        #         list_.append(node.val)
        #         if node.left:
        #             temp.append(node.left)
        #         if node.right:
        #             temp.append(node.right)
        #         level(temp, list_)
        # level(temp, list_)

        return node


s = Solution()
print(s.reConstructBinaryTree([1,2,4,7,3,5,6,8], [4,7,2,1,5,3,8,6]))



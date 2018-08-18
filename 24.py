# -*- coding:utf-8 -*-
"""
输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值
的和为输入整数的所有路径。路径定义为从树的根结点开始往
下一直到叶结点所经过的结点形成一条路径。(注意: 在返回
值的list中，数组长度大的数组靠前)
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.out = []
        self.temp_list = []

    # 返回二维列表，内部每个列表表示找到的路径：从任意结点出发
    def FindPathAllRoad(self, root, expectNumber):
        # write code here
        if root:
            self.findSingleNode(root, expectNumber, self.out, self.temp_list)
        if root.left:
            self.FindPathAllRoad(root.left, expectNumber)
        if root.right:
            self.FindPathAllRoad(root.right, expectNumber)
        return sorted(self.out, key=lambda x:len(x), reverse=True)

    # 返回二维列表，内部每个列表表示找到的路径:从根节点出发
    def FindPath(self, root, expectNumber, temp_list=list()):
        if not root:
            return self.out
        else:
            if root.val == expectNumber and not root.left and not root.right:
                temp_list1 = temp_list[:]
                temp_list1.append(root.val)
                self.out.append(temp_list1)
            elif root.val < expectNumber:
                temp_list1 = temp_list[:]
                temp_list1.append(root.val)
                expectNumber = expectNumber - root.val
                self.FindPath(root.left, expectNumber, temp_list1)
                self.FindPath(root.right, expectNumber, temp_list1)
            else:
                return self.out
        return sorted(self.out, key=lambda x:len(x), reverse=True)

    def findSingleNode(self, root, expectNumber, out, temp_list):
        if not root:
            return
        if root.val == expectNumber:
            temp_list1 = temp_list[:]
            temp_list1.append(root.val)
            out.append(temp_list1)
        elif root.val < expectNumber:
            temp_list1 = temp_list[:]
            temp_list1.append(root.val)
            expectNumber = expectNumber - root.val
            self.findSingleNode(root.left, expectNumber, out, temp_list1)
            self.findSingleNode(root.right, expectNumber, out, temp_list1)
        else:
            return


s = Solution()
tree1 = TreeNode(8)
tree1.left = TreeNode(8)
tree1.right = TreeNode(7)
tree1.left.left = TreeNode(9)
tree1.left.right = TreeNode(2)
tree1.left.left.left = TreeNode(4)
tree1.left.left.right = TreeNode(6)
tree1.left.right.left = TreeNode(6)
tree1.left.right.right = TreeNode(7)
tree1.right.left = TreeNode(3)
tree1.right.right = TreeNode(1)
# print(s.FindPathAllRoad(tree1, 18))
print(s.FindPath(tree1, 18))
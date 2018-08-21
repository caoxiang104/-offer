# -*- coding:utf-8 -*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.seris = ""
        self.index = 0

    def Serialize(self, root):
        # write code here
        if not root:
            return ""
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                self.seris += str(node.val) + ","
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        self.seris = self.seris[:len(self.seris) - 1]
        return self.seris

    def Deserialize(self, s):
        # write code here
        if self.index == 0:
            s = list(map(str, s.split(',')))
            self.index = 1
        if len(s) > 0:
            num = s.pop(0)
        else:
            return None
        root = None
        if num != "#":
            root = TreeNode(int(num))
            root.left = self.Deserialize(s)
            root.right = self.Deserialize(s)
        else:
            return None
        return root


s = Solution()
# tree1 = TreeNode(8)
# tree1.left = TreeNode(6)
# tree1.right = TreeNode(14)
# tree1.left.left = TreeNode(3)
# tree1.left.right = TreeNode('#')
# tree1.left.left.left = TreeNode("#")
# tree1.left.left.right = TreeNode(5)
# tree1.right.left = TreeNode(10)
# tree1.right.right = TreeNode("#")
# tree1.right.left.left = TreeNode("#")
# tree1.right.left.right = TreeNode(12)
tree1 = TreeNode(8)
tree1.left = TreeNode(6)
tree1.right = TreeNode(10)
tree1.left.left = TreeNode(5)
tree1.left.right = TreeNode(7)
tree1.right.left = TreeNode(9)
tree1.right.right = TreeNode(11)
out = s.Serialize(tree1)
print(out)
print(s.Serialize(s.Deserialize(out)))

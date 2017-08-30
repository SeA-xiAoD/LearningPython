# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        left_depth = self.depth(root.left)
        if left_depth == -1:
            return False
        right_depth = self.depth(root.right)
        if right_depth == -1:
            return False
        return abs(left_depth - right_depth) < 2

    def depth(self, root):
        if root == None:
            return 0
        left_depth = self.depth(root.left)
        if left_depth == -1:
            return -1
        right_depth = self.depth(root.right)
        if right_depth == -1:
            return -1
        if abs(left_depth - right_depth) > 1:
            return -1
        return max(left_depth, right_depth) + 1

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        if root.left != None and root.right == None:
            return self.searchDepth(root.left) + 1
        if root.left == None and root.right != None:
            return self.searchDepth(root.right) + 1
        return min(self.searchDepth(root.left), self.searchDepth(root.right)) + 1

    def searchDepth(self, root):
        if root.left == None and root.right == None:
            return 1
        if root.left != None and root.right == None:
            return self.searchDepth(root.left) + 1
        if root.left == None and root.right != None:
            return self.searchDepth(root.right) + 1
        return min(self.searchDepth(root.left), self.searchDepth(root.right)) + 1

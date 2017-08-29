# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        p = root.left
        q = root.right
        return self.isSym(root.left, root.right)

    def isSym(self, left, right):
        if left == None and right == None:
            return True
        if (left == None and right != None) or (left != None and right == None):
            return False
        if left.val != right.val:
            return False
        return self.isSym(left.left, right.right) and self.isSym(left.right, right.left)

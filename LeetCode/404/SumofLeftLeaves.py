# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        s = 0
        if root.left != None:
            s += self.dfs(root.left, 'l')
        if root.right != None:
            s += self.dfs(root.right, 'r')
        return s

    def dfs(self, root, tag):
        if root.left == None and root.right == None:
            if tag == 'l':
                return root.val
            else:
                return 0
        s = 0
        if root.left != None:
            s += self.dfs(root.left, 'l')
        if root.right != None:
            s += self.dfs(root.right, 'r')
        return s

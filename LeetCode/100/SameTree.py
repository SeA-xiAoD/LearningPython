# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return self.judgeSame(p, q)

    def judgeSame(self, p, q):
        if p == None and q == None:
            return True
        if (p == None and q != None) or (p != None and q == None):
            return False
        if p.val != q.val:
            return False
        return self.judgeSame(p.left, q.left) and self.judgeSame(p.right, q.right)

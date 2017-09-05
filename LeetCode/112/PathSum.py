# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False
        if root.left == None and root.right == None:
            return root.val == sum
        if root.left != None and root.right == None:
            return self.searchSum(root.left, sum - root.val)
        if root.left == None and root.right == None:
            return self.searchSum(root.right, sum - root.val)
        return self.searchSum(root.left, sum - root.val) or self.searchSum(root.right, sum - root.val)

    def searchSum(self, root, remian_sum):
        if root == None:
            return False
        if root.left == None and root.right == None:
            return root.val == remian_sum
        if root.left != None and root.right == None:
            return self.searchSum(root.left, remian_sum - root.val)
        if root.left == None and root.right == None:
            return self.searchSum(root.right, remian_sum - root.val)
        return self.searchSum(root.left, remian_sum - root.val) or self.searchSum(root.right, remian_sum - root.val)

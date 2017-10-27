# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.count = 0

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root == None:
            return self.count
        self.dfs(root, sum, 0)
        self.searchSum(root.left, sum)
        self.searchSum(root.right, sum)
        return self.count

    def searchSum(self, root, sum):
        if root == None:
            return
        self.dfs(root, sum, 0)
        self.searchSum(root.left, sum)
        self.searchSum(root.right, sum)

    def dfs(self, root, sum, now_sum):
        if root == None:
            return
        s = root.val + now_sum
        if s == sum:
            self.count += 1
        self.dfs(root.left, sum, s)
        self.dfs(root.right, sum, s)

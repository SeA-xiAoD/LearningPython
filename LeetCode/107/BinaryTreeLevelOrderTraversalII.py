# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        now_level = 0
        r = []

        r.insert(now_level, [])
        r[now_level].append(root.val)
        self.preOrder(root.left, now_level, r)
        self.preOrder(root.right, now_level, r)
        r.reverse()
        return r

    def preOrder(self, root, now_level, r):
        now_level += 1
        if root == None:
            return
        if len(r) <= now_level:
            r.insert(now_level, [])
        r[now_level].append(root.val)
        self.preOrder(root.left, now_level, r)
        self.preOrder(root.right, now_level, r)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def __init__(self):
        self.path_list = []
        self.stack = []

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root == None:
            return []
        self.stack.append(root.val)
        if root.left == None and root.right == None:
            path = str(self.stack[0])
            for i in range(1, len(self.stack)):
                path += '->'
                path += str(self.stack[i])
            self.path_list.append(path)
        self.deepSearch(root.left)
        self.deepSearch(root.right)
        return self.path_list

    def deepSearch(self, root):
        if root == None:
            return
        self.stack.append(root.val)
        if root.left == None and root.right == None:
            path = str(self.stack[0])
            for i in range(1, len(self.stack)):
                path += '->'
                path += str(self.stack[i])
            self.path_list.append(path)
        self.deepSearch(root.left)
        self.deepSearch(root.right)
        self.stack.pop(len(self.stack) - 1)

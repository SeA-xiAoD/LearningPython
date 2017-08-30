# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        root = TreeNode(nums[len(nums)//2])
        if len(nums)//2 == 0:
            return root
        else:
            root.left = self.sortedArrayToBST(nums[:len(nums)//2])
            root.right = self.sortedArrayToBST(nums[len(nums)//2+1:])
        return root

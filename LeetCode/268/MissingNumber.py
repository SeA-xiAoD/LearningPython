class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums) + 1
        number_set = set(nums)
        for i in range(0, length):
            if i not in number_set:
                return i

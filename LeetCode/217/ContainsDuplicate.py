class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        if length == 0 or length == 1:
            return False
        dupdir = {}
        for i in range(0, length):
            try:
                if dupdir[nums[i]] != -1:
                    return True
            except:
                dupdir[nums[i]] = i
        return False

class Solution(object):

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return 0
        if length == 1:
            return nums[0]
        last, now = 0, 0
        for number in nums:
            last, now = now, max(last + number, now)
        return now

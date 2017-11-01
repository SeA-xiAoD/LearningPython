class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        r = []
        for number in nums:
            index = abs(number) - 1
            nums[index] = -abs(nums[index])
        for i in range(0, len(nums)):
            if nums[i] > 0:
                r.append(i + 1)
        return r

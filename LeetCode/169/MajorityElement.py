class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return
        k = nums[0]
        count = 0
        for number in nums:
            if k == number:
                count += 1
            elif count == 0:
                k = number
            else:
                count -= 1
        return k

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)

        k = 0
        while(k < len(nums)-1):
            if nums[k] == nums[k+1]:
                nums.pop(k)
            else:
                k += 1

        return len(nums)

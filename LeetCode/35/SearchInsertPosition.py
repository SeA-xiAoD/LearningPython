class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            if nums[0] >= target:
                return 0
            else:
                return 1
        if nums[0] > target:
            return 0
        if nums[len(nums)-1] == target:
            return len(nums)-1
        if nums[len(nums)-1] < target:
            return len(nums)
        for i in range(0, len(nums)-1):
            if target == nums[i]:
                return i
            if target > nums[i] and target < nums[i+1]:
                return i+1

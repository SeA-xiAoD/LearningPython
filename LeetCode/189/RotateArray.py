class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        k = len(nums) - k
        for i in range(0, k//2):
            temp = nums[i]
            nums[i] = nums[k - i -1]
            nums[k - i - 1] = temp
        for i in range(k, k + (len(nums) - k)//2):
            temp = nums[i]
            nums[i] = nums[len(nums) - i + k -1]
            nums[len(nums) - i + k - 1] = temp
        for i in range(0, len(nums)//2):
            temp = nums[i]
            nums[i] = nums[len(nums) - i -1]
            nums[len(nums) - i - 1] = temp

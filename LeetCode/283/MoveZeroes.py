class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        now_pos = 0
        while now_pos < length:
            if nums[now_pos] == 0:
                nums.pop(now_pos)
                nums.append(0)
                length -= 1
            else:
                now_pos += 1

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return nums[0]
        dic = {}
        for number in nums:
            dic[number] = dic.get(number, 0) + 1
        for key in dic.keys():
            if dic[key] == 1:
                return key

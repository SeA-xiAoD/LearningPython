class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        length = len(nums)
        if length < 2:
            return False
        disdir = {}
        for i in range(0, length):
            try:
                if disdir[nums[i]] != -1:
                    if abs(i - disdir[nums[i]]) <= k:
                        return True
                    else:
                        disdir[nums[i]] = i
            except:
                disdir[nums[i]] = i
        return False

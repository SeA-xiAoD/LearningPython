class Solution(object):
    def twoSum(self, nums, target):
        hash_map = {}
        for i in range(0,len(nums)):
            hash_map[nums[i]] = i
        for i in range(0,len(nums)):
            temp = target - nums[i]
            if temp in hash_map.keys() and hash_map[temp] != i:
                return (i, hash_map[temp])
        return (-1, -1)

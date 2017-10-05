class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if nums == []:
            return
        self.nums = nums
        count = nums[0]
        self.sum_list = []
        length = len(nums)
        self.sum_list.append(count)
        for i in range(1, length):
            count += nums[i]
            self.sum_list.append(count)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if self.nums == []:
            return
        return self.sum_list[j] - self.sum_list[i] + self.nums[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

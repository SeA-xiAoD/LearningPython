class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i in range(0, len(numbers)):
            try:
                return (dic[numbers[i]] + 1, i + 1)
            except:
                dic[target - numbers[i]] = i

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = nums[0]
        tag = 0 # 0:only first 1:have second 2:have third
        second_num = 0
        third_num = 0
        for number in nums:
            if tag == 0:
                if number > max_num:
                    second_num = max_num
                    max_num = number
                    tag = 1
                elif number < max_num:
                    second_num = number
                    tag = 1
            elif tag == 1:
                if number > max_num:
                    third_num = second_num
                    second_num = max_num
                    max_num = number
                    tag = 2
                elif number > second_num and number < max_num:
                    third_num = second_num
                    second_num = number
                    tag = 2
                elif number < second_num:
                    third_num = number
                    tag = 2
            elif tag == 2:
                if number > max_num:
                    third_num = second_num
                    second_num = max_num
                    max_num = number
                elif number > second_num and number < max_num:
                    third_num = second_num
                    second_num = number
                elif number > third_num and number < second_num:
                    third_num = number
        if tag == 0 or tag == 1:
            return max_num
        else:
            return third_num

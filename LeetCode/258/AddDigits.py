class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            return num
        r = num % 9
        if r == 0:
            return 9
        return r
